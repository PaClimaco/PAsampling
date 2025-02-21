Introduction
==========================================================


Passive Sampling (PAsampling) is a repository designed to provide easy and fast access to existing and novel tools and resources for data sampling. This project aims to facilitate the implementation of data sampling techniques and provide insights on key aspects of data selection in machine learning, with a particular focus on training data selection for optimizing regression model performance. The term "Passive" refers to the fact that the library mainly focuses on selection approaches that rely solely on data feature representations and do not involve any active learning procedures, which require iterative learning of one or several models. Additionally, the library provides tools for creating machine learning experiment pipelines.

Features
--------

- PAsampling includes several data sampling methods:\
   - `Density Aware Farthest Point (DAFPS) <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/native_functions/da_fps.py>`_
   - `FacilityLocation <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/wrappers/facility_location_sampler.py>`_
   - `Farthest Point Sampling (FPS)  <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/native_functions/fps.py>`_ 
   - `FPS_Plus <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/wrappers/modified_samplers.py>`_
   - `k-medoids++ <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/wrappers/kmedoids_sampler.py>`_
   - `Twin <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/wrappers/twin_sampler.py>`_
   
- ML pipeline tools:\
   - `DataLoader <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/utils/data_loader.py>`_
   - `DataSelector <https://github.com/PaClimaco/PAsampling/tree/main/PAsampling/utils/data_selection.py>`_

Installation
------------

To install the PAsampling package, you can either install it via PyPI or clone the repository and install the required dependencies:

Install via PyPI
~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install PAsampling

Install via Git
~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/PaClimaco/PAsampling.git
   cd PAsampling
   pip install .

Usage
-----

Here is a basic example of how to use PAsampling:

.. code-block:: python

   from PAsampling import *
   # Example usage (Farthest Point Sampling on QM dataset)

   datasets =  DataLoader('./data') # data_loader function
   x, labels = datasets.QM7_dataset()
   fps_sampler = FPS()  # FPS sampler class
   fps_indices = fps_sampler.fit(x, initial_subset=[0], b_samples=100)  # Fit FPS to data matrix

Tutorials
---------

Explore the tutorials to learn how to use the PAsampling library tools and gain key insights into data sampling in machine learning.
   - `Basic key concepts <https://github.com/PaClimaco/PAsampling/blob/main/Tutorials/basic_concepts.ipynb>`_
   - `Training data selection for regression model performance optimization <https://github.com/PaClimaco/PAsampling/blob/main/Tutorials/Training_data_selection.ipynb>`_

Contributing
------------

We welcome contributions! Please read our `contributing guidelines <https://github.com/PaClimaco/PAsampling/blob/main/CONTRIBUTING.md>`_ to get started. All contributors will be acknowledged and credited.

Contact
-------

For any questions or inquiries, please contact us at `climaco@ins.uni-bonn.de <mailto:climaco@ins.uni-bonn.de>`_.

Dependencies
------------

Some of the functions implemented in PAsampling are wraps of functions from the following existing libraries:

- `Apricot <https://github.com/jmschrei/apricot>`_ (MIT License)
- `twinning <https://github.com/avkl/twinning>`_ (Apache 2.0 License)

