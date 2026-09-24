from setuptools import find_packages, setup

package_name = 'dofbot_telemetry'

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
    maintainer='Felipe Rivas',
    maintainer_email='rivascf@gmail.com',
    description='Dofbot Telemetry package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'telemtry_info = dofbot_telemetry.Telemetry:init_node',
            'telemtry_sub = dofbot_telemetry.TelemetrySubs:init_node'
        ],
    },
)
