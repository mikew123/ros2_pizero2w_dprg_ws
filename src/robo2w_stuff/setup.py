from setuptools import find_packages, setup

package_name = 'robo2w_stuff'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'gpiozero'],
    zip_safe=True,
    maintainer='robo2w',
    maintainer_email='mikew123@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'led_node = robo2w_stuff.led_node:main',
            'hcsr04_node = robo2w_stuff.hcsr04_node:main',
        ],
    },
)
