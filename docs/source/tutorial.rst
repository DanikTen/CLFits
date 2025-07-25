Tutorial
========

This tutorial provides a walkthrough of a common task: correcting a FITS header keyword.

The Problem
-----------

Imagine you've just completed an observation, but you realize the object's name was incorrectly logged in the FITS header. Instead of "NGC 4993", it was saved as "NGC 101". `CLFits` allows you to correct this with a single command.

Step 1: View the Header (Optional)
----------------------------------

First, you can view the current header to confirm the error.

.. code-block:: bash

   clfits view your_image.fits

This will print the full header, where you would see a line like:

.. code-block:: none

   OBJECT  = 'NGC 101'           / Name of the observed object

Step 2: Set the Correct Keyword Value
-------------------------------------

Now, use the `set` command to update the `OBJECT` keyword to its correct value. You can also add a comment to document the change.

.. code-block:: bash

   clfits set your_image.fits OBJECT "NGC 4993" --comment "Corrected object name from log"

Step 3: Verify the Change
-------------------------

You can verify the change by either viewing the header again or using the `get` command.

.. code-block:: bash

   clfits get your_image.fits OBJECT

The output should now be:

.. code-block:: none

   NGC 4993

That's it! You've successfully corrected the FITS header using `CLFits`.

Bonus: Exporting the Header
---------------------------

Now that your header is corrected, you might want to save it to a more common format for archiving or for use in other scripts. The `export` command makes this easy.

**Export to a JSON file:**

You can save the header to a file, inferring the format from the filename:

.. code-block:: bash

   clfits export your_image.fits --output corrected_header.json

**Export to YAML and print to console:**

If you don't provide an output file, the result is printed to the console.

.. code-block:: bash

   clfits export your_image.fits --format yaml 