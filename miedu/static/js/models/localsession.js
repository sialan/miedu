define([
    'underscore',
    'backbone',
    'localstorage',
], function(_, Backbone) {

	var LocalSessionModel = Backbone.Model.extend({
		localStorage: new Backbone.LocalStorage("session"),
        defaults: {
			current_page: "",
            last_page: "",
            session_key: "AAACEdEose0cBAFsCu8E7u6Nm5JZAfZBDLtBV5NfNUG1gYI3uNatNi4bWS9H6sY0SHzgCp1untttuCS2VN7HZCEU9NfPSvWLA9PYTlnpkAZDZD",
            account_id: 10110101,
            facebook_id: "10110101",
            dp_url: "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash4/203315_501227993_1401624842_q.jpg",
            full_name: "Jane Doe",
            challenges_extended: 0,
            videos_created: 0,
            age: 18,
            sex: "F",
            unread: 0,
            new_user: false,
            connected: "not_connected",
            current_capture_challenge_id: 0,
            current_capture_video_id: "0",
            current_capture_video_length: 0,
            current_capture_friend_id: 0,
            current_log_id: 0,
		},
	});
	return LocalSessionModel;
});