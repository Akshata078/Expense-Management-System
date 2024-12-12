# Copyright (c) 2024, AKshata and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LeaveApplication(Document):
    def before_submit(self):
        self.validate_leave_quota()

    def validate_leave_quota(self):
        leave_quota = frappe.get_doc("Leave Quota", {"employee": self.employee_name})

        for leave_type in leave_quota.leave_information:
            if leave_type.leave_type == self.leave_type:  
                leave_balance = leave_type.maximum_leave_allowed - leave_type.leave_taken

                if self.total_days > leave_balance:
                    frappe.throw(f"Insufficient leave balance. Available: {leave_balance} days.")
                else:
                    leave_type.leave_taken += self.total_days  
                    leave_type.leave_balance = leave_type.maximum_leave_allowed - leave_type.leave_taken  
                    leave_quota.save()

                break 
