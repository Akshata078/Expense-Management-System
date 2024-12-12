// Copyright (c) 2024, AKshata and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave Application", {
	refresh(frm) {

	},
    start_date(frm){
        calculateEmployeeLeaveCount(frm)
    },
    end_date(frm){
        calculateEmployeeLeaveCount(frm)
    }
});

function calculateEmployeeLeaveCount(frm){
        let startDate = new Date(frm.doc.start_date);
        let endDate = new Date(frm.doc.end_date);
        let dateDifference = endDate - startDate;
        let dateCount = dateDifference / (1000*3600*24);
        frm.set_value("total_days", dateCount + 1)
}
