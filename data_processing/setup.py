from setuptools import find_packages, setup

package_name = 'data_processing'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/gps.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='leeeju',
    author_email='02stu4@gmail.com',
    maintainer='leeeju',
    maintainer_email='02stu4@gmail.com',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='test avoidance',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_processing = data_processing.gps_processing:main',
        ],
    },
)
