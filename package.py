name = "ocio_configs_aces"

version = "1.0.0"


# --------------------------------------------
# NOTE: The build system will NOT generate the ocio config files.
# This needs to be done prior to rez-build / rez-release.
# Here are the steps to generate the ocio config files:
#
# 1) in a shell, create a rez environment with the following requests:
# rez-env python-3 requests invoke ocio jsonpickle
#
# 2) From the resulting environment, append the root of this repo to the PYTHONPATH:
# (replace the path with your root location)
# export PYTHONPATH=$PYTHONPATH:/home/marcelosercheli/devel/ext/OpenColorIO-Config-ACES
#
# 3) from the shell, run the following "invoke" command:
# invoke clean build-config-cg build-config-studio
# --------------------------------------------


authors = [
    "Academy Software Foundation",
]

description = \
    """
    LUTs for OCIO ACES
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"
uuid = "repository.OpenColorIO-Configs-ACES"

def commands():

    env.REZ_OCIO_CONFIGS_ACES_ROOT = "{root}"
    env.OCIO = "{root}/config/aces/cg-config-v1.0.0_aces-v1.3_ocio-v2.1.ocio"
