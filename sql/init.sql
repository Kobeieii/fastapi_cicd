DROP TABLE IF EXISTS `pets`;
CREATE TABLE `pets` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `type` varchar(10) NOT NULL,
  `sound` varchar(25) NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL
) ;

INSERT INTO `pets` (`id`, `name`, `type`, `sound`) VALUES
(1, 'Toob', 'Dog', 'Bark'),
(2, 'Sood Loar', 'Cat', 'Meow'),
(3, 'Jibb', 'Bird', 'Chirp');