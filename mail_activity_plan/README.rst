====================
mail_activity_plan
====================

Installation
============
Use Odoo normal module installation procedure to install ``mail_activity_plan``.


Configuration
=============

To create activities plans, go to Settings > Technical > Discuss > Activity plans :

Provice a name

Add activity templates :

Select an activity type, write a summary. Optionnaly assigne to a user and write a note.

A plan can be related to many activity templates

A activity template can be related to only one plan

A activity template is related to only one activity type


Usage
=====
Once your plan is configured, you can define a server-action to launch automatically the activities for a choose model

Go to Settings > Technical > Actions > Server Actions

Provide a name, select a model, select action "[generate_activities]", select a plan.

Once your new server action is configured, go to an instance of the chosen model, 
click on the server action to generate automatically the activities of the plan.

If nobody is assigned to a activity, the current user will be automatically assigned.

Known issues / Roadmap
======================

None yet.

Bug Tracker
===========

Bugs are tracked on `our issues website <https://github.com/elabore-coop/ux-tools/issues>`_. In case of
trouble, please check there if your issue has already been
reported. If you spotted it first, help us smashing it by providing a
detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Laetitia Da Costa (https://github.com/LaetitiaElabore)

Funders
-------

The development of this module has been financially supported by:
* Elabore (https://elabore.coop)


Maintainer
----------

This module is maintained by Elabore.