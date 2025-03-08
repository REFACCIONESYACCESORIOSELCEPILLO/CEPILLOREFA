from . import models

def _update_order_lock_drat(env):
	env.cr.execute("UPDATE sale_order SET blocked_order=True WHERE state='draft';")