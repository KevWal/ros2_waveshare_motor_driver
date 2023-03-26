from setuptools import setup

package_name = 'ros2_waveshare_motor_driver'

setup(
 name=package_name,
 version='0.0.1',
 packages=[package_name],
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 maintainer='Kevin Walton',
 maintainer_email='kevin@unseen.org',
 description='ROS 2 Driver Package for the PCA9685 based Waveshare Motor Driver HAT on a Rasperbery Pi for a two-wheeled differential drive and castor robot.',
 license='TODO: License declaration',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'my_node = ros2_waveshare_motor_driver.my_node:main'
     ],
   },
)