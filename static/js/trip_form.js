/**
 * Validates the Trip form submission.
 * - Prevents submitting trips with invalid time ranges.
 * - Prevents overlapping trips unless marked as overnight.
 * Also manages display of validation error messages.
 */
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("trip-form");
    const startInput = document.getElementById("trip-start-time");
    const endInput = document.getElementById("trip-finish-time");
    const overnightCheckbox = document.getElementById("is-overnight");
    const errorBox = document.getElementById("js-validation-error");

    form.addEventListener("submit", function (event) {
        hideError();

        const start = startInput.value;
        const end = endInput.value;
        const isOvernight = overnightCheckbox.checked;

        /**
         * Skip validation if either time input is missing.
         */
        if (!start || !end) return;

        /**
         * Check if trip is invalid (not overnight but ends before it starts).
         */
        if (!isOvernight && end <= start) {
            showError("Trip finish time must be after the trip start time unless the trip is overnight.");
            event.preventDefault();
            return;
        }

        /**
         * Prevent overlapping trips unless marked as overnight.
         */
        if (!isOvernight && isOverlapping(start, end, existingTrips)) {
            showError("This trip overlaps with an existing trip.");
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

/**
 * Checks if a new trip overlaps with any existing trips.
 */
function isOverlapping(start, end, existingTrips) {
    const newStart = toMinutes(start);
    const newEnd = toMinutes(end);

    return existingTrips.some(trip => {
        const tripStart = toMinutes(trip.trip_start_time);
        const tripEnd = toMinutes(trip.trip_finish_time);

        return newStart < tripEnd && newEnd > tripStart;
    });
}

/**
 * Converts time into total minutes.
 */
function toMinutes(timeStr) {
    const [hours, minutes] = timeStr.split(":").map(Number);
    return hours * 60 + minutes;
}