from setuptools import find_packages, setup

package_name = 'dofbot_agent'

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
    description='Dofbot IA Agent package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ai_agent = dofbot_agent.ai_agent:init_node',
            'agent_action_srv = dofbot_agent.ai_agent_action_srv:init_node',
            'agent_action_client = dofbot_agent.dofbot_agent_client:init_node'
        ],
    },
)
