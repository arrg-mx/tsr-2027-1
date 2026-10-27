from setuptools import find_packages, setup
# Para agrgar mas carpetas o folders, archivos y otros elementos necesarios
# para la ejecusion del paquete se agrega la libreria del SO
import os
from glob import glob

package_name = 'dofbot_config'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Felipe Rivas',
    maintainer_email='rivascf@gmail.com',
    description='Dofbot Configuration package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'param_srv = dofbot_config.parameter_srv:init_node'
        ],
    },
)
