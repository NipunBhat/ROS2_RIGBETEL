from setuptools import find_packages, setup

package_name = 'turtlesim_assignment'

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
    maintainer='nipun',
    maintainer_email='bhatnipun29@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'displace_turtle=turtlesim_assignment.move_turtle:main',
            'square_open_loop=turtlesim_assignment.open_loop.square_open:main',
            'triangle_open_loop=turtlesim_assignment.open_loop.triangle_open:main',
            'star_open_loop=turtlesim_assignment.open_loop.star_open_loop:main',
        ],
    },
)
