function toggleLike(eventId) {
    var likeButton = $(".like-button[data-event-id='" + eventId + "']");
    var isLiked = likeButton.hasClass("liked");

    $.ajax({
        url: isLiked ? '/unlike_event/' + eventId : '/like_event/' + eventId,
        type: 'POST',
        success: function(data) {
            likeButton.find('.like-count').text(data.likes);
            likeButton.toggleClass("liked", !isLiked);
        },
    });
}

function toggleDislike(eventId) {
    var dislikeButton = $(".dislike-button[data-event-id='" + eventId + "']");
    var isDisliked = dislikeButton.hasClass("disliked");

    $.ajax({
        url: isDisliked ? '/undislike_event/' + eventId : '/dislike_event/' + eventId,
        type: 'POST',
        success: function(data) {
            dislikeButton.find('.dislike-count').text(data.dislikes);
            dislikeButton.toggleClass("disliked", !isDisliked);
        },
    });
}

$(document).ready(function() {
    $('.like-button').click(function() {
        var eventId = $(this).data('event-id');
        toggleLike(eventId);
    });

    $('.dislike-button').click(function() {
        var eventId = $(this).data('event-id');
        toggleDislike(eventId);
    });
});
