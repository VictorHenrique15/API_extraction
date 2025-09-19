create TABLE nasa_apod (
	id SERIAL primary key,
	title TEXT,
	date DATE,
	explanation TEXT,
	url TEXT,
	hdurl TEXT,
	media_type TEXT,
	copyright TEXT
);


select * from nasa_apod;

SELECT * FROM nasa_apod ORDER BY date DESC;
