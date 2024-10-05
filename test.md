# Assignment I - Compiling a Custom Linux Kernel & Adding New System Calls


## Environment Setting

### 1. Install Linux

![image](https://hackmd.io/_uploads/SJc41saAC.png)

- Download .iso
- Use VMware Workstation
- Resource: 8GB RAM, 6 core, 70GB SSD

### 2. Download the Linux kernel source 

![image](https://hackmd.io/_uploads/rkYk2QNR0.png)
- Clone the repository, using ``--depth=1 --branch v6.1 --single-branch`` to speed up and save disk space

## Compiling the Linux Kernel

### 1. Change kernel local version

![image](https://hackmd.io/_uploads/ryq5TIEC0.png)
- Revise the Makefile (``EXTRAVERSION=os-313551036``)

:::success
### After compiling the linux kernel:

![image](https://hackmd.io/_uploads/S1VsfxrAA.png)
![image](https://hackmd.io/_uploads/r1DRzeHCA.png)
- ``uname -a`` can see the local version
- ``make kernelrelease`` can make sure our version name is meet the homework requirement before compiling
:::

### 2. Compiling the linux kernel

![image](https://hackmd.io/_uploads/HkSbbL4CC.png)
- ``make menuconfig`` can change the config file in text menu interface
- I keep the default setting 

![image](https://hackmd.io/_uploads/Bkljub8V0A.png)
- Compile the linux kernel 
- ``-jx`` can set ``x`` cores to speed up the process of compiling

![image](https://hackmd.io/_uploads/HydHeq4CA.png)
- Install the kernel module

![image](https://hackmd.io/_uploads/BkmprkrAC.png)
- Install the kernel in the ``/boot``, and update grub automatically
- After completing all the steps, run ``sudo reboot`` and press ``<ESC>`` to go into ``grub``
- You can load your own kernel version in the ``grub`` 


## Implementing a new System Calls

### 1. Define the system call

![image](https://hackmd.io/_uploads/H1h-KENAC.png)
- ``linux/include/linux/syscalls.h``
- ``asmlinkage`` forces function parameters to be passed via the stack instead of registers, commonly used in system call implementations

![image](https://hackmd.io/_uploads/SyK-5VERA.png)
- ``linux/include/uapi/asm-generic/unistd.h``
- Define new system call number (e.g., 451)
- Total system call add one


![image](https://hackmd.io/_uploads/ByU4jEV0R.png)
- ``linux/kernel/sys_ni.c`` 
- ``COND_SYSCALL`` conditionally enables a system call, ensuring it either invokes the implemented function or returns ``-ENOSYS`` if the function is not defined or disabled.

![image](https://hackmd.io/_uploads/rkALS35CC.png)
- ``linux/arch/x86/entry/syscalls/syscall_64.tbl``
- Add the system call to the x86_64 syscall table

### 2. System call implementation


### ``revstr/Makefile``
```make=
obj-y := revstr.o
```


### ``revstr/revstr.c``
```c=
#include <linux/kernel.h>
#include <linux/syscalls.h>

SYSCALL_DEFINE2(revstr, char *, user_str, size_t, n)
{
    // get string from user
    char rev_str[100];
    char kernel_str[100];
    
    if(copy_from_user(kernel_str, user_str, n))
            return -EFAULT;
    
    // reverse string
    for(int i = 0; i < (int)n; i++) {
        rev_str[i] = kernel_str[n - 1 - i];
    }
    kernel_str[n] = '\0';
    rev_str[n] = '\0';

    // print info into kernel buffer
    printk(KERN_INFO "The origin string: %s\n", kernel_str);    
    printk(KERN_INFO "The reversed string: %s\n", rev_str);    
    
    // save string back to user
    if(copy_to_user(user_str, rev_str, n))
               return -EFAULT;
	
    return 0;
} 

```
- ``mkdir revstr`` create a folder, ``cd`` this folder
- Add a ``.c`` file (e.g., revstr.c) that implement the function and add the Makefile
- ``obj-y := revstr.o`` means revstr.o will compile and link into kernel
- Implementaion details:
    - Use ``SYSCALL_DEFINE2`` to define revstr system call
    - Function name, parameters and the corresponding type should be passed into ``SYSCALL_DEFINE2``
    - ``copy_from_user`` can copy user space data into kernel sapace; ``copy_to_user`` can copy kernel space data into user sapace
    - ``printk`` can write messages into kernel ring buffer and ``dmesg`` can see these messages

![image](https://hackmd.io/_uploads/ByUmlYCCC.png)

- ``/linux/Makefile``
- Add revstr folder in ``core-y`` and ensure revstr can be included into kernel


### 3. Test system call

![image](https://hackmd.io/_uploads/SJuE-Y0AC.png)
- After compiling the linux kernel, test the sample code

![image](https://hackmd.io/_uploads/HJntbt000.png)
- Use ``sudo dmesg`` to see the kernel ring buffer

## Patch and Packlist

### 1. Generate patch
![image](https://hackmd.io/_uploads/SkvY3KCRR.png)
- git add and commit, generating the patch file

![image](https://hackmd.io/_uploads/SJgDaYR0C.png)
- Reset to HEAD (v6.1)

![image](https://hackmd.io/_uploads/HyICTFRCA.png)
- Apply patch (warning does not impact patch's functionality) 

### 2. Generate packlist
![image](https://hackmd.io/_uploads/BJLJaF0RC.png)
- Generate packlist

![image](https://hackmd.io/_uploads/SJE-TKARC.png)
- Packlist context