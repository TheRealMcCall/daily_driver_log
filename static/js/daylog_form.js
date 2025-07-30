/**
 * Validates the DayLog form submission.
 * - Prevents duplicate logs.
 * - Prevents future-dated logs.
 * - Prevents logs older than 2 days.
 * Also manages display of JavaScript-based error messages.
 */
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("daylog-form");
    const startInput = document.getElementById("start-date");
    const errorBox = document.getElementById("js-validation-error");

    form.addEventListener("submit", function (event) {
        hideError();

        const start = new Date(startInput.value);
        const today = new Date();
        const twoDaysAgo = new Date();
        twoDaysAgo.setDate(today.getDate() - 2);

        /**
         * Normalize all dates to midnight to ensure correct comparisons.
         */
        [start, today, twoDaysAgo].forEach(d => d.setHours(0, 0, 0, 0));

        const selectedDate = startInput.value;

        /**
         * Check if a DayLog already exists for the selected date.
         */
        if (typeof existingDates !== "undefined" && existingDates.includes(selectedDate)) {
            showError("A DayLog for this date already exists.");
            event.preventDefault();
            return;
        }

        /**
         * Check if the selected date is in the future.
         */
        if (start > today) {
            showError("You cannot create logs for future dates.");
            event.preventDefault();
            return;
        }

        /**
         * Check if the selected date is older than two days.
         */
        if (start < twoDaysAgo) {
            showError("You can only create logs from the last 2 days.");
            event.preventDefault();
            return;
        }
    });

    /**
     * Displays a validation error message on the form.
     */
    function showError(message) {
        errorBox.textContent = message;
        errorBox.classList.remove("d-none");
    }

    /**
     * Clears and hides the error message box.
     */
    function hideError() {
        errorBox.textContent = "";
        errorBox.classList.add("d-none");
    }
});