.. _authentication:

Authentication
==============

Ekaayam exposes several interfaces and hooks to customize authentication and
implementations of these. For details on the hooks see :ref:`hooks`

Authentication Interfaces
-------------------------

.. module:: flaskbb.core.auth.authentication

.. autoclass:: AuthenticationManager
   :members:
   :undoc-members:

.. autoclass:: AuthenticationProvider
   :members:
   :undoc-members:

.. autoclass:: PostAuthenticationHandler
   :members:
   :undoc-members:

.. autoclass:: AuthenticationFailureHandler
   :members:
   :undoc-members:


Authentication Provided Implementations
---------------------------------------

.. module:: flaskbb.auth.services.authentication
.. autoclass:: DefaultEkaayamAuthProvider
.. autoclass:: MarkFailedLogin
.. autoclass:: BlockUnactivatedUser
.. autoclass:: ClearFailedLogins
.. autoclass:: PluginAuthenticationManager


Reauthentication Interfaces
---------------------------

.. module:: flaskbb.core.auth.authentication
   :noindex:

.. autoclass:: ReauthenticateManager
   :members:
   :undoc-members:

.. autoclass:: ReauthenticateProvider
   :members:
   :undoc-members:

.. autoclass:: PostReauthenticateHandler
   :members:
   :undoc-members:

.. autoclass:: ReauthenticateFailureHandler
   :members:
   :undoc-members:


Reauthentication Provided Implementations
-----------------------------------------

.. module:: flaskbb.auth.services.reauthentication
.. autoclass:: DefaultEkaayamReauthProvider
.. autoclass:: ClearFailedLoginsOnReauth
.. autoclass:: MarkFailedReauth
.. autoclass:: PluginReauthenticationManager


Exceptions
----------

.. module:: flaskbb.core.auth.authentication
   :noindex:

.. autoexception:: StopAuthentication
.. autoexception:: ForceLogout
