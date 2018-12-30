from glob import glob
import os
import tempfile
import tarfile
from urllib.request import urlretrieve
import setuptools
import shutil

VERSION = '3.1'

# Download and unpack the correct tarballs
# Pick those up from http://openrefine.org/download.html
def provision():
    linux_url = f'https://github.com/OpenRefine/OpenRefine/releases/download/{VERSION}/openrefine-linux-{VERSION}.tar.gz'

    dest_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'openrefine',
        'extracted'
    )
    shutil.rmtree(dest_path, ignore_errors=True)
    with tempfile.NamedTemporaryFile() as tar_file, tempfile.TemporaryDirectory() as extract_dir:
        urlretrieve(linux_url, tar_file.name)
        tf = tarfile.open(tar_file.name)
        tf.extractall(extract_dir)
        shutil.move(os.path.join(extract_dir, f'openrefine-{VERSION}'), dest_path)

provision()

setuptools.setup(
    name="openrefine-bin",
    version=VERSION,
    url="https://github.com/yuvipanda/openrefine-bin",
    author="Yuvi Panda",
    author_email='yuvipanda@gmail.com',
    description="Binary package distribution of OpenRefine",
    packages=setuptools.find_packages(),
    package_data={
        '*': 'openrefine/extracted/*'
    },
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'refine = openrefine:main'
        ]
    }
)
