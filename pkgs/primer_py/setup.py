from setuptools import find_packages, setup

package_name = 'primer_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arrgusr',
    maintainer_email='erik.pena@ingenieria.unam.edu',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publicador_py = primer_py.primer_nodo:main',
            'ejemplo_1_py = primer_py.ejemplo_1:main',
            'ejemplo_2_py = primer_py.ejemplo_2:main',
            'subcriptor_py = primer_py.subcriptor:main'
        ],
    },
)
