from PIL import Image,ImageEnhance,ImageFilter
import sys
import os
import math
import random
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm

import copy
import shutil
import time
import io
from torch import bfloat16 as bfloat16
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import resnet
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

save_dir = 'pretrain_save'

y_pred = []
y_true = []
train_loss = []
test_loss = []
train_acc = []
test_acc = []


def split_data(orig_dir):
    train_dir = 'data_split/train'
    val_dir = 'data_split/val'
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    train_pct = 0.66
    for root, dirs, files in os.walk(orig_dir):
        for sub_dir in dirs:
            imgs = os.listdir(os.path.join(root, sub_dir))
            imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
            random.shuffle(imgs)
            img_count = len(imgs)
            boundary = round(img_count * train_pct)

            for i in range(img_count):
                if i < boundary:
                    out_dir = os.path.join(train_dir, sub_dir)
                else:
                    out_dir = os.path.join(val_dir, sub_dir)
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                target_path = os.path.join(out_dir, imgs[i])
                src_path = os.path.join(orig_dir, sub_dir, imgs[i])
                shutil.copy(src_path, target_path)
        
        # print('Class:{}, train:{}, valid:{}'.format(sub_dir, boundary, img_count - boundary))
    
    for root, dirs, files in os.walk(orig_dir):
        for sub_dir in dirs:
            imgs = os.listdir(os.path.join(root, sub_dir))
            imgs = list(filter(lambda x: x.endswith('.jpeg'), imgs))
            random.shuffle(imgs)
            img_count = len(imgs)
            boundary = round(img_count * train_pct)

            for i in range(img_count):
                if i < boundary:
                    out_dir = os.path.join(train_dir, sub_dir)
                else:
                    out_dir = os.path.join(val_dir, sub_dir)
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                target_path = os.path.join(out_dir, imgs[i])
                src_path = os.path.join(orig_dir, sub_dir, imgs[i])
                shutil.copy(src_path, target_path)
        
        # print('Class:{}, train:{}, valid:{}'.format(sub_dir, boundary, img_count - boundary))

    for root, dirs, files in os.walk(orig_dir):
        for sub_dir in dirs:
            imgs = os.listdir(os.path.join(root, sub_dir))
            imgs = list(filter(lambda x: x.endswith('.png'), imgs))
            random.shuffle(imgs)
            img_count = len(imgs)
            boundary = round(img_count * train_pct)

            for i in range(img_count):
                if i < boundary:
                    out_dir = os.path.join(train_dir, sub_dir)
                else:
                    out_dir = os.path.join(val_dir, sub_dir)
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                target_path = os.path.join(out_dir, imgs[i])
                src_path = os.path.join(orig_dir, sub_dir, imgs[i])
                shutil.copy(src_path, target_path)
        
        # print('Class:{}, train:{}, valid:{}'.format(sub_dir, boundary, img_count - boundary))

    return train_dir, val_dir


def main():
    global y_pred, y_true, train_loss, test_loss, train_acc, test_acc, save_dir

    pathTest = "data_split"
    try:
        shutil.rmtree(pathTest)
    except OSError as e:
        print(e)
    else:
        print("The directory is deleted successfully")
    train_path, val_path = split_data('data')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    normalize = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.1, 0.1, 0.1])
    #normalize = transforms.Normalize(mean=[0.491, 0.482, 0.446], std=[0.247, 0.243, 0.261])
    #normalize只適用於tensor，如果沒有要轉成numpy，那用這個不會有問題，只是圖片的顏色會被normalize。
        
    img_lb = datasets.ImageFolder(root = train_path, transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(45, resample=False, expand=False, center=None),
        transforms.RandomCrop(64, padding=None, pad_if_needed=True, fill=0, padding_mode='constant'),
        # transforms.ColorJitter(brightness=(0, 5), contrast=(0, 5), saturation=(0, 5), hue=(-0.1, 0.1)),
        normalize,
    ]))


    val_img_lb = datasets.ImageFolder(root = val_path, transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(45, resample=False, expand=False, center=None),
        transforms.RandomCrop(64, padding=None, pad_if_needed=True, fill=0, padding_mode = 'constant'),
        # transforms.ColorJitter(brightness=(0, 5), contrast=(0, 5), saturation=(0, 5), hue=(-0.1, 0.1)),
        normalize,
    ]))

    model = resnet.__dict__['resnet20']()
    model.cuda()

    cudnn.benchmark = True

    train_loader = torch.utils.data.DataLoader(
        img_lb, batch_size=32, shuffle=True, num_workers=8, pin_memory=True)
    val_loader = torch.utils.data.DataLoader(
        val_img_lb, batch_size=32, shuffle=False, num_workers=8, pin_memory=True)

    criterion = nn.CrossEntropyLoss().cuda()

    # optimizer裡的參數都可以調整
    # optimizer = torch.optim.SGD(model.parameters(), 
    #                             5e-5,
    #                             momentum=0.9,
    #                             weight_decay=1e-1)
    optimizer = torch.optim.Adam(model.parameters(),
                                lr=5e-5,
                                betas=(0.9, 0.999),
                                eps=1e-08,
                                weight_decay=1e-1)

    lr_scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer,
                                                        milestones=[50, 100, 150], 
                                                        last_epoch=-1)

    best_prec1 = 0.0
    for epoch in range(0, 200):
        # train for one epoch
        train(train_loader, model, criterion, optimizer, epoch, train_loss, train_acc)
        lr_scheduler.step()

        # evaluate on validation set
        prec1 = validate(val_loader, model, criterion, test_loss, test_acc)

        # remember best prec@1 and save checkpoint
        is_best = prec1 > best_prec1
        best_prec1 = max(prec1, best_prec1)

        if epoch > 0 and epoch % 10 == 0:
            save_checkpoint({
                'epoch': epoch + 1,
                'state_dict': model.state_dict(),
                'best_prec1': best_prec1,
                'is_best': is_best
            }, filename=os.path.join('pretrain_save', 'checkpoint.th'))

        save_checkpoint({
            'state_dict': model.state_dict(),
            'best_prec1': best_prec1,
            'is_best': is_best
        }, filename=os.path.join('pretrain_save', 'model.th'))
    
    # generate loss curve
    generate_loss_curve(train_loss, test_loss)

    # generate accuracy curve
    generate_acc_curve(train_acc, test_acc)

    # generate confusion matrix
    conf_mat(val_loader, model, y_pred, y_true)


def generate_loss_curve(train_loss, test_loss):
    plt.plot(train_loss, label = 'loss')
    plt.plot(test_loss, label = 'val_loss')
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'valid'], loc = 'upper left')
    plt.savefig(os.path.join(save_dir, 'loss.png'))
    plt.close()
    return


def generate_acc_curve(train_acc, test_acc):
    plt.plot(train_acc, label = 'accuracy')
    plt.plot(test_acc, label = 'val_accuracy')
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'valid'], loc = 'upper left')
    plt.savefig(os.path.join(save_dir, 'accuracy.png'))
    plt.close()
    return


def conf_mat(val_loader, model, y_pred, y_true):
    model.eval()
    y_pred.clear()
    y_true.clear()

    with torch.no_grad():
        for i, (input, label) in enumerate(val_loader):
            input_var = input.cuda()
            label_var = label.cuda()
            
            output = model(input_var)
            _, preds = torch.max(output, 1)

            y_pred.extend(preds.view(-1).detach().cpu().numpy())
            y_true.extend(label_var.view(-1).detach().cpu().numpy())
    
    # make confusion matrix
    cf_matrix = confusion_matrix(y_true, y_pred)

    # compute accuracy of each class
    per_cls_acc = cf_matrix.diagonal() / cf_matrix.sum(axis=1)
    print('accuracy of each class:', per_cls_acc)

    cf_matrix = pd.DataFrame(cf_matrix) #(index:true, col:pred)
    print('Plot confusion matrix:\n', cf_matrix)

    return cf_matrix.values


def train(train_loader, model, criterion, optimizer, epoch, train_loss, train_acc):
    """
        Run one train epoch
    """
    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    # switch to train mode
    model.train()

    end = time.time()
    for i, (input, label) in enumerate(train_loader):
        # measure data loading time
        data_time.update(time.time() - end)
        
        input_var = input.cuda()
        label_var = label.cuda()

        output = model(input_var)
        loss = criterion(output, label_var)

        # compute gradient and do SGD step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        output = output.float()
        loss = loss.float()

        # measure accuracy and record loss
        prec1 = accuracy(output.data, label)[0]
        losses.update(loss.item(), input.size(0))
        top1.update(prec1.item(), input.size(0))

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % 50 == 0:
            print('Epoch: [{0}][{1}/{2}]\t'
                  'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                  'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'
                  'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                  'Prec@1 {top1.val:.3f} ({top1.avg:.3f})'
                  .format(epoch, i, len(train_loader), batch_time=batch_time,
                    data_time=data_time, loss=losses, top1=top1))
    
    # record train loss, accuracy
    train_loss.append(losses.avg)
    train_acc.append(top1.avg)

    return


def validate(val_loader, model, criterion, test_loss, test_acc):
    """
    Run evaluation
    """
    batch_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    # switch to evaluate mode
    model.eval()

    end = time.time()
    with torch.no_grad():
        for i, (input, label) in enumerate(val_loader):
            input_var = input.cuda()#.float()
            label_var = label.cuda()

            # compute output
            output = model(input_var)
            loss = criterion(output, label_var)

            output = output.float()
            loss = loss.float()

            # measure accuracy and record loss
            prec1 = accuracy(output.data, label)[0]
            losses.update(loss.item(), input.size(0))
            top1.update(prec1.item(), input.size(0))

            # measure elapsed time
            batch_time.update(time.time() - end)
            end = time.time()

            if i % 50 == 0:
                print('Test: [{0}/{1}]\t'
                      'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                      'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                      'Prec@1 {top1.val:.3f} ({top1.avg:.3f})'
                      .format(i, len(val_loader), batch_time=batch_time, 
                        loss=losses, top1=top1))
    
    # record test loss, accuracy
    test_loss.append(losses.avg)
    test_acc.append(top1.avg)

    print(' * Prec@1 {top1.avg:.3f}'.format(top1=top1))

    return top1.avg


def save_checkpoint(state, filename='checkpoint.pth.tar'):
    """
    Save the training model
    """
    torch.save(state, filename)


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t().to()
    target = target.to(pred.device)
    correct = pred.eq(target.reshape(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].reshape(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


if __name__ == '__main__':
    main()
