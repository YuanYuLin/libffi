import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
src_usr_lib_dir = ""
dst_usr_lib_dir = ""
src_include_dir = ""
dst_include_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global src_usr_lib_dir
    global dst_usr_lib_dir
    global src_include_dir
    global dst_include_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    if arch == "armhf":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabihf")
    elif arch == "armel":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabi")
    elif arch == "x86_64":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/x86_64-linux-gnu")
    else:
        sys.exit(1)
    dst_usr_lib_dir = ops.path_join(output_dir, "usr/lib")

    src_include_dir = iopc.getBaseRootFile("usr/include")
    dst_include_dir = ops.path_join("include",args["pkg_name"])


def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.mkdir(dst_usr_lib_dir)
    ops.copyto(ops.path_join(src_usr_lib_dir, "libffi.so.6.0.4"), dst_usr_lib_dir)
    ops.ln(dst_usr_lib_dir, "libffi.so.6.0.4", "libffi.so.6.0")
    ops.ln(dst_usr_lib_dir, "libffi.so.6.0.4", "libffi.so.6")
    ops.ln(dst_usr_lib_dir, "libffi.so.6.0.4", "libffi.so")
    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(build_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)
    return False

def MAIN_INSTALL(args):
    set_global(args)

    iopc.installBin(args["pkg_name"], ops.path_join(dst_usr_lib_dir, "."), "usr/lib") 
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

