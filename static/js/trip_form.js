const existingTrips = JSON.parse(
    document.getElementById("existing-trips-data").textContent
);
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("trip-form");
    const startInput = document.getElementById("id_trip_start_time");
    const endInput = document.getElementById("id_trip_finish_time");
    const overnightCheckbox = document.getElementById("id_is_overnight");
    const errorBox = document.getElementById("js-validation-error");

    form.addEventListener("submit", function (event) {
        hideError();

        const start = startInput.value;
        const end = endInput.value;
        const isOvernight = overnightCheckbox.checked;

        if (!start || !end) return;

        if (!isOvernight && end <= start) {
            showError("Trip finish time must be after the trip start time unless the trip is overnight.");
            event.preventDefault();
            return;
        }

        if (!isOvernight && isOverlapping(start, end, existingTrips)) {
            showError("This trip overlaps with an existing trip.");
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

function isOverlapping(start, end, existingTrips) {
    const newStart = toMinutes(start);
    const newEnd = toMinutes(end);

    return existingTrips.some(trip => {
        const tripStart = toMinutes(trip.trip_start_time);
        const tripEnd = toMinutes(trip.trip_finish_time);

        return newStart < tripEnd && newEnd > tripStart;
    });
}

function toMinutes(timeStr) {
    const [hours, minutes] = timeStr.split(":").map(Number);
    return hours * 60 + minutes;
}