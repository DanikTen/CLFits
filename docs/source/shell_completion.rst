Shell Completion
================

`CLFits` uses `Typer`, which comes with built-in support for shell completion.
This can make using the CLI much faster and easier.

Enabling Completion
-------------------

To activate shell completion, you need to run an installation command specific
to your shell.

**Bash**

Add the following to your `~/.bashrc` or `~/.bash_profile`:

.. code-block:: bash

   eval "$(_CLFITS_COMPLETE=bash_source clfits)"

**Zsh**

Add the following to your `~/.zshrc`:

.. code-block:: bash

   eval "$(_CLFITS_COMPLETE=zsh_source clfits)"

**Fish**

Add the following to your `~/.config/fish/completions/clfits.fish`:

.. code-block:: bash

   _CLFITS_COMPLETE=fish_source clfits > ~/.config/fish/completions/clfits.fish

After adding the appropriate line, restart your shell or source the configuration
file for the changes to take effect. 