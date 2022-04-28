-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2022 at 01:22 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tpi`
--

-- --------------------------------------------------------

--
-- Table structure for table `dl`
--

CREATE TABLE `dl` (
  `id` int(11) NOT NULL,
  `package-name` text NOT NULL,
  `dl-link` text NOT NULL,
  `author` text NOT NULL,
  `version` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dl`
--

INSERT INTO `dl` (`id`, `package-name`, `dl-link`, `author`, `version`) VALUES
(1, 'win-rar', 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe', 'Eugene Roshal', '6.11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dl`
--
ALTER TABLE `dl`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dl`
--
ALTER TABLE `dl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
