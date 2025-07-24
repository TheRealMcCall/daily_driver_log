document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("daylog-form");
    const startInput = document.getElementById("id_start_date");
    const errorBox = document.getElementById("js-validation-error");

    form.addEventListener("submit", function (event) {
        hideError();

        const start = new Date(startInput.value);
        const today = new Date();
        const twoDaysAgo = new Date();
        twoDaysAgo.setDate(today.getDate() - 2);

        // Reset time for all dates to midnight to avoid timezone mismatch
        [start, today, twoDaysAgo].forEach(d => d.setHours(0, 0, 0, 0));

        const selectedDate = startInput.value;

        if (typeof existingDates !== "undefined" && existingDates.includes(selectedDate)) {
            showError("A DayLog for this date already exists.");
            event.preventDefault();
            return;
        }

        if (start > today) {
            showError("You cannot create logs for future dates.");
            event.preventDefault();
            return;
        }

        if (start < twoDaysAgo) {
            showError("You can only create logs from the last 2 days.");
            event.preventDefault();
            return;
        }
    });

    function showError(message) {
        errorBox.textContent = message;
        errorBox.classList.remove("d-none");
    }

    function hideError() {
        errorBox.textContent = "";
        errorBox.classList.add("d-none");
    }
});