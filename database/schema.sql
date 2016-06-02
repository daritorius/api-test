drop table if exists assets;
drop table if exists credits;
drop table if exists thumbnails;
drop table if exists credits_assets;

create table assets (
  id INTEGER NOT NULL,
  title VARCHAR(254),
  description VARCHAR(254) NULL,
  created_at DATETIME,
  PRIMARY KEY (id)
);

create table credits (
  id INTEGER NOT NULL,
  name VARCHAR(80),
  PRIMARY KEY (id)
);

create table credits_assets (
  id INTEGER NOT NULL,
  assets_id INTEGER,
  credits_id INTEGER,
  PRIMARY KEY (id)
);

create table thumbnails (
  id INTEGER NOT NULL,
  image_url VARCHAR(254),
  asset_id INTEGER,
  PRIMARY KEY (id)
);


insert into assets (title, description, created_at) values (
  'Wiredrive IOWA: Wiredrive Award Winners 2009',
  'https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b',
  '2016-06-01 00:00:00');

insert into assets (title, description, created_at) values (
  'Wiredrive IOWA: Wiredrive Award Winners 2010',
  'https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1',
  '2016-05-31 00:00:00');


insert into credits (name) values ('Fozie Bear');
insert into credits (name) values ('Big Bird');
insert into credits (name) values ('Angry Tiger');


insert into thumbnails (image_url, asset_id) values ('https://upload.wikimedia.org/wikipedia/commons/3/36/Hopetoun_falls.jpg', 1);
insert into thumbnails (image_url, asset_id) values ('http://www.planwallpaper.com/static/images/2ba7dbaa96e79e4c81dd7808706d2bb7_large.jpg', 1);
insert into thumbnails (image_url, asset_id) values ('http://www.planwallpaper.com/static/images/2ba7dbaa96e79e4c81dd7808706d2bb7_large.jpg', 2);
insert into thumbnails (image_url, asset_id) values ('http://www.planwallpaper.com/static/images/nature.jpg', 2);


insert into credits_assets (assets_id, credits_id) values (1, 1);
insert into credits_assets (assets_id, credits_id) values (1, 2);
insert into credits_assets (assets_id, credits_id) values (1, 3);
insert into credits_assets (assets_id, credits_id) values (2, 1);
insert into credits_assets (assets_id, credits_id) values (2, 2);
