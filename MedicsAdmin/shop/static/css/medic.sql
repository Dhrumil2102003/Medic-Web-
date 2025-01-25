-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2023 at 11:31 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medic`
--

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `AreaId` int(11) NOT NULL,
  `AreaName` varchar(25) NOT NULL,
  `pinCode` varchar(6) NOT NULL,
  `CityId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`AreaId`, `AreaName`, `pinCode`, `CityId_id`) VALUES
(1, 'Bapunager', '382350', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add area', 7, 'add_area'),
(26, 'Can change area', 7, 'change_area'),
(27, 'Can delete area', 7, 'delete_area'),
(28, 'Can view area', 7, 'view_area'),
(29, 'Can add blog category', 8, 'add_blogcategory'),
(30, 'Can change blog category', 8, 'change_blogcategory'),
(31, 'Can delete blog category', 8, 'delete_blogcategory'),
(32, 'Can view blog category', 8, 'view_blogcategory'),
(33, 'Can add category', 9, 'add_category'),
(34, 'Can change category', 9, 'change_category'),
(35, 'Can delete category', 9, 'delete_category'),
(36, 'Can view category', 9, 'view_category'),
(37, 'Can add health condition', 10, 'add_healthcondition'),
(38, 'Can change health condition', 10, 'change_healthcondition'),
(39, 'Can delete health condition', 10, 'delete_healthcondition'),
(40, 'Can view health condition', 10, 'view_healthcondition'),
(41, 'Can add order', 11, 'add_order'),
(42, 'Can change order', 11, 'change_order'),
(43, 'Can delete order', 11, 'delete_order'),
(44, 'Can view order', 11, 'view_order'),
(45, 'Can add order status', 12, 'add_orderstatus'),
(46, 'Can change order status', 12, 'change_orderstatus'),
(47, 'Can delete order status', 12, 'delete_orderstatus'),
(48, 'Can view order status', 12, 'view_orderstatus'),
(49, 'Can add payment status', 13, 'add_paymentstatus'),
(50, 'Can change payment status', 13, 'change_paymentstatus'),
(51, 'Can delete payment status', 13, 'delete_paymentstatus'),
(52, 'Can view payment status', 13, 'view_paymentstatus'),
(53, 'Can add payment type', 14, 'add_paymenttype'),
(54, 'Can change payment type', 14, 'change_paymenttype'),
(55, 'Can delete payment type', 14, 'delete_paymenttype'),
(56, 'Can view payment type', 14, 'view_paymenttype'),
(57, 'Can add role', 15, 'add_role'),
(58, 'Can change role', 15, 'change_role'),
(59, 'Can delete role', 15, 'delete_role'),
(60, 'Can view role', 15, 'view_role'),
(61, 'Can add state', 16, 'add_state'),
(62, 'Can change state', 16, 'change_state'),
(63, 'Can delete state', 16, 'delete_state'),
(64, 'Can view state', 16, 'view_state'),
(65, 'Can add sub category', 17, 'add_subcategory'),
(66, 'Can change sub category', 17, 'change_subcategory'),
(67, 'Can delete sub category', 17, 'delete_subcategory'),
(68, 'Can view sub category', 17, 'view_subcategory'),
(69, 'Can add vendor', 18, 'add_vendor'),
(70, 'Can change vendor', 18, 'change_vendor'),
(71, 'Can delete vendor', 18, 'delete_vendor'),
(72, 'Can view vendor', 18, 'view_vendor'),
(73, 'Can add user', 19, 'add_user'),
(74, 'Can change user', 19, 'change_user'),
(75, 'Can delete user', 19, 'delete_user'),
(76, 'Can view user', 19, 'view_user'),
(77, 'Can add sub sub category', 20, 'add_subsubcategory'),
(78, 'Can change sub sub category', 20, 'change_subsubcategory'),
(79, 'Can delete sub sub category', 20, 'delete_subsubcategory'),
(80, 'Can view sub sub category', 20, 'view_subsubcategory'),
(81, 'Can add store', 21, 'add_store'),
(82, 'Can change store', 21, 'change_store'),
(83, 'Can delete store', 21, 'delete_store'),
(84, 'Can view store', 21, 'view_store'),
(85, 'Can add product', 22, 'add_product'),
(86, 'Can change product', 22, 'change_product'),
(87, 'Can delete product', 22, 'delete_product'),
(88, 'Can view product', 22, 'view_product'),
(89, 'Can add payment', 23, 'add_payment'),
(90, 'Can change payment', 23, 'change_payment'),
(91, 'Can delete payment', 23, 'delete_payment'),
(92, 'Can view payment', 23, 'view_payment'),
(93, 'Can add medicine', 24, 'add_medicine'),
(94, 'Can change medicine', 24, 'change_medicine'),
(95, 'Can delete medicine', 24, 'delete_medicine'),
(96, 'Can view medicine', 24, 'view_medicine'),
(97, 'Can add feed back', 25, 'add_feedback'),
(98, 'Can change feed back', 25, 'change_feedback'),
(99, 'Can delete feed back', 25, 'delete_feedback'),
(100, 'Can view feed back', 25, 'view_feedback'),
(101, 'Can add city', 26, 'add_city'),
(102, 'Can change city', 26, 'change_city'),
(103, 'Can delete city', 26, 'delete_city'),
(104, 'Can view city', 26, 'view_city');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blogcategory`
--

CREATE TABLE `blogcategory` (
  `BlogId` int(11) NOT NULL,
  `BlogType` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `CatId` int(11) NOT NULL,
  `CatName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`CatId`, `CatName`) VALUES
(1, 'Baby Care'),
(2, 'Health & Nutrition'),
(3, 'Women Care'),
(4, 'Personal Care'),
(5, 'Ayurveda');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `CityId` int(11) NOT NULL,
  `CityName` varchar(25) NOT NULL,
  `StateId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`CityId`, `CityName`, `StateId_id`) VALUES
(1, 'Ahmedabad', 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'MedicsAdminApp', 'area'),
(8, 'MedicsAdminApp', 'blogcategory'),
(9, 'MedicsAdminApp', 'category'),
(26, 'MedicsAdminApp', 'city'),
(25, 'MedicsAdminApp', 'feedback'),
(10, 'MedicsAdminApp', 'healthcondition'),
(24, 'MedicsAdminApp', 'medicine'),
(11, 'MedicsAdminApp', 'order'),
(12, 'MedicsAdminApp', 'orderstatus'),
(23, 'MedicsAdminApp', 'payment'),
(13, 'MedicsAdminApp', 'paymentstatus'),
(14, 'MedicsAdminApp', 'paymenttype'),
(22, 'MedicsAdminApp', 'product'),
(15, 'MedicsAdminApp', 'role'),
(16, 'MedicsAdminApp', 'state'),
(21, 'MedicsAdminApp', 'store'),
(17, 'MedicsAdminApp', 'subcategory'),
(20, 'MedicsAdminApp', 'subsubcategory'),
(19, 'MedicsAdminApp', 'user'),
(18, 'MedicsAdminApp', 'vendor'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'MedicsAdminApp', '0001_initial', '2023-03-03 21:12:03.722238'),
(2, 'MedicsAdminApp', '0002_alter_category_catname_alter_subcategory_subcatname_and_more', '2023-03-03 21:12:03.767510'),
(3, 'MedicsAdminApp', '0003_remove_store_storeimage', '2023-03-03 21:12:03.787594'),
(4, 'MedicsAdminApp', '0004_remove_product_catid', '2023-03-03 21:12:04.007929'),
(5, 'contenttypes', '0001_initial', '2023-03-03 21:12:04.038415'),
(6, 'auth', '0001_initial', '2023-03-03 21:12:04.443204'),
(7, 'admin', '0001_initial', '2023-03-03 21:12:04.532823'),
(8, 'admin', '0002_logentry_remove_auto_add', '2023-03-03 21:12:04.543865'),
(9, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-03 21:12:04.549878'),
(10, 'contenttypes', '0002_remove_content_type_name', '2023-03-03 21:12:04.629129'),
(11, 'auth', '0002_alter_permission_name_max_length', '2023-03-03 21:12:04.678598'),
(12, 'auth', '0003_alter_user_email_max_length', '2023-03-03 21:12:04.703103'),
(13, 'auth', '0004_alter_user_username_opts', '2023-03-03 21:12:04.711378'),
(14, 'auth', '0005_alter_user_last_login_null', '2023-03-03 21:12:04.751635'),
(15, 'auth', '0006_require_contenttypes_0002', '2023-03-03 21:12:04.751635'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2023-03-03 21:12:04.767641'),
(17, 'auth', '0008_alter_user_username_max_length', '2023-03-03 21:12:04.792077'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2023-03-03 21:12:04.810087'),
(19, 'auth', '0010_alter_group_name_max_length', '2023-03-03 21:12:04.833119'),
(20, 'auth', '0011_update_proxy_permissions', '2023-03-03 21:12:04.859620'),
(21, 'auth', '0012_alter_user_first_name_max_length', '2023-03-03 21:12:04.874270'),
(22, 'sessions', '0001_initial', '2023-03-03 21:12:04.898269');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('b70epjpq2fqi363mruzyyxmzon2yaei7', '.eJyrVkpMyc3Mi0_NTczMUbJSSskoKi0rSMxLqUw0NLFwSAcJ6yXn5yrpQBUWJBYXA9UZGhmbmJqZW1jCJTJTlKwMdZTKUvNS8ovg5iVlJJZlZucm5pUn5mWaWViimAhVi8VIqAzYzFoAsPM1xA:1pYDkw:MQd50C2MiU5vK1Vrnpj_PqvM7UZ73IRTBwzVcyvu9No', '2023-03-17 22:20:02.590943');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `FeedBackId` int(11) NOT NULL,
  `FeedBackDate` date NOT NULL,
  `FeedBackDesc` varchar(250) NOT NULL,
  `UserId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `healthcondition`
--

CREATE TABLE `healthcondition` (
  `HCId` int(11) NOT NULL,
  `HCName` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `BatchId` int(11) NOT NULL,
  `Company` varchar(15) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `MFG` date NOT NULL,
  `EXPDate` date NOT NULL,
  `Qty` int(11) NOT NULL,
  `HCId_id` int(11) NOT NULL,
  `ProductId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `OrderId` int(11) NOT NULL,
  `OrderDate` date NOT NULL,
  `OrderStatusId_id` int(11) NOT NULL,
  `ProductId_id` int(11) NOT NULL,
  `UserId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orderstatus`
--

CREATE TABLE `orderstatus` (
  `OrderStatusId` int(11) NOT NULL,
  `Status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `PaymentId` int(11) NOT NULL,
  `PaymentAmunt` int(11) NOT NULL,
  `PaymentDate` date NOT NULL,
  `OrderId_id` int(11) NOT NULL,
  `PaymentStatusId_id` int(11) NOT NULL,
  `PaymentTypeId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `paymentstatus`
--

CREATE TABLE `paymentstatus` (
  `PaymentStatusId` int(11) NOT NULL,
  `PaymentStatus` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `paymenttype`
--

CREATE TABLE `paymenttype` (
  `PaymentTypeId` int(11) NOT NULL,
  `PaymentType` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `ProductId` int(11) NOT NULL,
  `ProductImage` varchar(100) NOT NULL,
  `ProductName` varchar(25) NOT NULL,
  `ProductPrice` decimal(7,2) NOT NULL,
  `ProductQty` int(11) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `BestSeller` tinyint(1) NOT NULL,
  `Featured` tinyint(1) NOT NULL,
  `Trending` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `MRP` int(11) NOT NULL,
  `HCId_id` int(11) NOT NULL,
  `StoreId_id` int(11) NOT NULL,
  `SubCatId_id` int(11) NOT NULL,
  `SubSubCatId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `RoleId` int(11) NOT NULL,
  `RoleName` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`RoleId`, `RoleName`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `StateId` int(11) NOT NULL,
  `StateName` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`StateId`, `StateName`) VALUES
(1, 'Gujarat');

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `StoreId` int(11) NOT NULL,
  `StoreName` varchar(30) NOT NULL,
  `StoreAddress` varchar(150) NOT NULL,
  `LicenseNumber` int(11) NOT NULL,
  `StoreMobile` bigint(20) NOT NULL,
  `VendorId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE `subcategory` (
  `SubCatId` int(11) NOT NULL,
  `SubCatName` varchar(20) NOT NULL,
  `CatId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`SubCatId`, `SubCatName`, `CatId_id`) VALUES
(2, 'Diapering', 1),
(3, 'Baby Food', 1),
(4, 'Baby Hair Care', 1),
(5, 'Baby Skin Care', 1),
(6, 'Baby Food By Age', 1),
(7, 'Health Drinks', 2),
(8, 'Minerals', 2),
(9, 'Weight Management', 2),
(10, 'Sports Nutrition', 2),
(11, 'Feminine Hygiene', 3),
(12, 'Women Supplements', 3),
(13, 'Pregnancy  Grooming', 3),
(14, 'Breast Feeding', 1),
(15, 'Herbs', 5),
(16, 'Health Concerns', 5),
(17, 'Hair Care', 4),
(18, 'Skin Care', 4),
(19, 'Sexual Wellness', 4),
(20, 'Mens Grooming', 4);

-- --------------------------------------------------------

--
-- Table structure for table `subsubcategory`
--

CREATE TABLE `subsubcategory` (
  `SubSubCatId` int(11) NOT NULL,
  `SubSubCatName` varchar(20) NOT NULL,
  `SubCatId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subsubcategory`
--

INSERT INTO `subsubcategory` (`SubSubCatId`, `SubSubCatName`, `SubCatId_id`) VALUES
(1, 'Diapers', 2),
(2, 'Wipes', 2),
(3, 'Baby Cereals', 3),
(4, 'Formula Milk', 3),
(5, 'Baby Shampoos', 4),
(6, 'Baby Hair Oils', 4),
(7, 'Baby Creams', 5),
(8, 'Baby Lotions', 5),
(9, 'Baby Massage Oils', 5),
(10, 'Baby Lip Balms', 5),
(11, 'Baby Sunscreens', 5),
(12, 'Baby Powders', 5),
(13, 'Rash Creams', 5),
(14, 'Preterm', 6),
(15, '0 to 6 Months', 6),
(16, '6 to 12 Months', 6),
(17, '12 to 18 Months', 6),
(18, '18 to 24 Months', 2),
(19, 'Above 2 Years', 6),
(20, 'Manual Breast Pump', 14),
(21, 'Electric Breast Pump', 14),
(22, 'Breast Pads', 14),
(23, 'Nipple Shields', 14),
(24, 'Nipple Puller', 14),
(25, 'Sanitary Pads', 11),
(26, 'Menstrual Cups', 11),
(27, 'Tampons', 11),
(28, 'Panty Liners', 11),
(29, 'Intimate Care', 11),
(30, 'Nutritional Drinks', 12),
(31, 'Health Tonics', 12),
(32, 'Women Multivitamins', 12),
(33, 'Hair Removal', 13),
(34, 'Razors & Cartridges', 13),
(35, 'Calcium', 8),
(36, 'Iron', 8),
(37, 'Magnesium', 8),
(38, 'Zinc', 8),
(39, 'Sugar Substitutes', 9),
(40, 'Fat Burner Supply', 9),
(41, 'Weight Gain Supply', 9),
(42, 'Meal Replacements', 9),
(43, 'Green Tea', 9),
(44, 'Adult Nutrition', 7),
(45, 'Kids Nutrition', 7),
(46, 'Energy Drinks', 7),
(47, 'Apple Cider Vinegar', 7),
(48, 'Honey', 7),
(49, 'Protein Powders', 10),
(50, 'Whey Protein', 10),
(51, 'Muscle Mass Builders', 10),
(52, 'Protein Bars', 10),
(53, 'Pre Workout', 10),
(54, 'Post Workout', 10),
(55, 'Amla', 15),
(56, 'Tulsi', 15),
(57, 'Aloe Vera', 15),
(58, 'Ashwagandha', 15),
(59, 'Giloy', 15),
(60, 'Triphala', 15),
(61, 'Shilajit', 15),
(62, 'Neem', 15),
(63, 'Haldi', 15),
(64, 'Cold & Cough', 16),
(65, 'Diabetic Care', 16),
(66, 'Abdomen Care', 16),
(67, 'Liver Care', 16),
(68, 'Sexual Health Care', 16),
(69, 'Immunity Boosters', 16),
(70, 'Hair & Nails Care', 16),
(71, 'Condoms', 19),
(72, 'Performance Enhancer', 19),
(73, 'Shaving Brush', 20),
(74, 'Catridges', 20),
(75, 'Shaving Creams', 20),
(76, 'After Shave Lotions', 20),
(77, 'Hair Oils', 17),
(78, 'Conditioners', 17),
(79, 'Shampoos', 17),
(80, 'Gels & Serums', 17),
(81, 'Hair Creams & Packs', 17),
(82, 'Hair Colors', 17),
(83, 'Accessories', 17),
(84, 'Bath & Body', 18),
(85, 'Face Care', 18),
(86, 'Beauty', 18),
(87, 'Lip Care', 18),
(88, 'Foot & Hand Care', 18),
(89, 'Facial Wipes', 18),
(90, 'Massage Oils', 18),
(91, 'Hand Wash Sanitizers', 18);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserId` int(11) NOT NULL,
  `UserName` varchar(25) NOT NULL,
  `UserProfile` varchar(100) DEFAULT NULL,
  `FirstName` varchar(15) NOT NULL,
  `LastName` varchar(15) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Mobile` bigint(20) NOT NULL,
  `Password` varchar(25) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `otp` int(11) DEFAULT NULL,
  `otp_used` int(11) DEFAULT NULL,
  `AreaId_id` int(11) NOT NULL,
  `RoleId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserId`, `UserName`, `UserProfile`, `FirstName`, `LastName`, `DOB`, `Gender`, `Email`, `Mobile`, `Password`, `Address`, `otp`, `otp_used`, `AreaId_id`, `RoleId_id`) VALUES
(1, 'Dhruv', 'img/vendor/u1.jpg', 'Dhruv', 'Pandya', '2013-04-21', 'Male', 'dhruvpandya148@gmail.com', 7486902405, '123456789', 'Bapunager', NULL, NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--

CREATE TABLE `vendor` (
  `VendorId` int(11) NOT NULL,
  `Profile` varchar(100) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Mobile` bigint(20) NOT NULL,
  `Password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vendor`
--

INSERT INTO `vendor` (`VendorId`, `Profile`, `Name`, `Email`, `Mobile`, `Password`) VALUES
(1, 'img/vendor/u1.jpg', 'Bhavik', 'bhavikmanwani689@gmail.com', 9990445041, '123456789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`AreaId`),
  ADD KEY `Area_CityId_id_76432886_fk_City_CityId` (`CityId_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `blogcategory`
--
ALTER TABLE `blogcategory`
  ADD PRIMARY KEY (`BlogId`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CatId`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`CityId`),
  ADD KEY `City_StateId_id_eea264a3_fk_State_StateId` (`StateId_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`FeedBackId`),
  ADD KEY `FeedBack_UserId_id_58118fd2_fk_user_UserId` (`UserId_id`);

--
-- Indexes for table `healthcondition`
--
ALTER TABLE `healthcondition`
  ADD PRIMARY KEY (`HCId`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`BatchId`),
  ADD KEY `Medicine_HCId_id_3c68804f_fk_HealthCondition_HCId` (`HCId_id`),
  ADD KEY `Medicine_ProductId_id_3f2caf7f_fk_Product_ProductId` (`ProductId_id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`OrderId`),
  ADD KEY `Order_OrderStatusId_id_c4f19a14_fk_OrderStatus_OrderStatusId` (`OrderStatusId_id`),
  ADD KEY `Order_ProductId_id_5ac894ec_fk_Product_ProductId` (`ProductId_id`),
  ADD KEY `Order_UserId_id_4ab039dc_fk_user_UserId` (`UserId_id`);

--
-- Indexes for table `orderstatus`
--
ALTER TABLE `orderstatus`
  ADD PRIMARY KEY (`OrderStatusId`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`PaymentId`),
  ADD KEY `Payment_OrderId_id_a927ef87_fk_Order_OrderId` (`OrderId_id`),
  ADD KEY `Payment_PaymentStatusId_id_1d605eac_fk_PaymentSt` (`PaymentStatusId_id`),
  ADD KEY `Payment_PaymentTypeId_id_69f2a828_fk_PaymentType_PaymentTypeId` (`PaymentTypeId_id`);

--
-- Indexes for table `paymentstatus`
--
ALTER TABLE `paymentstatus`
  ADD PRIMARY KEY (`PaymentStatusId`);

--
-- Indexes for table `paymenttype`
--
ALTER TABLE `paymenttype`
  ADD PRIMARY KEY (`PaymentTypeId`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ProductId`),
  ADD KEY `Product_HCId_id_20a7620b_fk_HealthCondition_HCId` (`HCId_id`),
  ADD KEY `Product_StoreId_id_3d9aa094_fk_Store_StoreId` (`StoreId_id`),
  ADD KEY `Product_SubCatId_id_b80b11bd_fk_SubCategory_SubCatId` (`SubCatId_id`),
  ADD KEY `Product_SubSubCatId_id_6c4a15db_fk_SubSubCategory_SubSubCatId` (`SubSubCatId_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`RoleId`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`StateId`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`StoreId`),
  ADD UNIQUE KEY `LicenseNumber` (`LicenseNumber`),
  ADD KEY `Store_VendorId_id_d45fdff4_fk_Vendor_VendorId` (`VendorId_id`);

--
-- Indexes for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`SubCatId`),
  ADD KEY `SubCategory_CatId_id_165293ca_fk_Category_CatId` (`CatId_id`);

--
-- Indexes for table `subsubcategory`
--
ALTER TABLE `subsubcategory`
  ADD PRIMARY KEY (`SubSubCatId`),
  ADD KEY `SubSubCategory_SubCatId_id_62789346_fk_SubCategory_SubCatId` (`SubCatId_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserId`),
  ADD UNIQUE KEY `UserName` (`UserName`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Mobile` (`Mobile`),
  ADD KEY `user_AreaId_id_b4ede9b1_fk_Area_AreaId` (`AreaId_id`),
  ADD KEY `user_RoleId_id_e40ba351_fk_Role_RoleId` (`RoleId_id`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`VendorId`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Mobile` (`Mobile`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `AreaId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blogcategory`
--
ALTER TABLE `blogcategory`
  MODIFY `BlogId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `CatId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `CityId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `FeedBackId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `healthcondition`
--
ALTER TABLE `healthcondition`
  MODIFY `HCId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `BatchId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `OrderId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orderstatus`
--
ALTER TABLE `orderstatus`
  MODIFY `OrderStatusId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `PaymentId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paymentstatus`
--
ALTER TABLE `paymentstatus`
  MODIFY `PaymentStatusId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paymenttype`
--
ALTER TABLE `paymenttype`
  MODIFY `PaymentTypeId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `ProductId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `RoleId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `StateId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `StoreId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `SubCatId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `subsubcategory`
--
ALTER TABLE `subsubcategory`
  MODIFY `SubSubCatId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `VendorId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `area`
--
ALTER TABLE `area`
  ADD CONSTRAINT `Area_CityId_id_76432886_fk_City_CityId` FOREIGN KEY (`CityId_id`) REFERENCES `city` (`CityId`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `City_StateId_id_eea264a3_fk_State_StateId` FOREIGN KEY (`StateId_id`) REFERENCES `state` (`StateId`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `FeedBack_UserId_id_58118fd2_fk_user_UserId` FOREIGN KEY (`UserId_id`) REFERENCES `user` (`UserId`);

--
-- Constraints for table `medicine`
--
ALTER TABLE `medicine`
  ADD CONSTRAINT `Medicine_HCId_id_3c68804f_fk_HealthCondition_HCId` FOREIGN KEY (`HCId_id`) REFERENCES `healthcondition` (`HCId`),
  ADD CONSTRAINT `Medicine_ProductId_id_3f2caf7f_fk_Product_ProductId` FOREIGN KEY (`ProductId_id`) REFERENCES `product` (`ProductId`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `Order_OrderStatusId_id_c4f19a14_fk_OrderStatus_OrderStatusId` FOREIGN KEY (`OrderStatusId_id`) REFERENCES `orderstatus` (`OrderStatusId`),
  ADD CONSTRAINT `Order_ProductId_id_5ac894ec_fk_Product_ProductId` FOREIGN KEY (`ProductId_id`) REFERENCES `product` (`ProductId`),
  ADD CONSTRAINT `Order_UserId_id_4ab039dc_fk_user_UserId` FOREIGN KEY (`UserId_id`) REFERENCES `user` (`UserId`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `Payment_OrderId_id_a927ef87_fk_Order_OrderId` FOREIGN KEY (`OrderId_id`) REFERENCES `order` (`OrderId`),
  ADD CONSTRAINT `Payment_PaymentStatusId_id_1d605eac_fk_PaymentSt` FOREIGN KEY (`PaymentStatusId_id`) REFERENCES `paymentstatus` (`PaymentStatusId`),
  ADD CONSTRAINT `Payment_PaymentTypeId_id_69f2a828_fk_PaymentType_PaymentTypeId` FOREIGN KEY (`PaymentTypeId_id`) REFERENCES `paymenttype` (`PaymentTypeId`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `Product_HCId_id_20a7620b_fk_HealthCondition_HCId` FOREIGN KEY (`HCId_id`) REFERENCES `healthcondition` (`HCId`),
  ADD CONSTRAINT `Product_StoreId_id_3d9aa094_fk_Store_StoreId` FOREIGN KEY (`StoreId_id`) REFERENCES `store` (`StoreId`),
  ADD CONSTRAINT `Product_SubCatId_id_b80b11bd_fk_SubCategory_SubCatId` FOREIGN KEY (`SubCatId_id`) REFERENCES `subcategory` (`SubCatId`),
  ADD CONSTRAINT `Product_SubSubCatId_id_6c4a15db_fk_SubSubCategory_SubSubCatId` FOREIGN KEY (`SubSubCatId_id`) REFERENCES `subsubcategory` (`SubSubCatId`);

--
-- Constraints for table `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `Store_VendorId_id_d45fdff4_fk_Vendor_VendorId` FOREIGN KEY (`VendorId_id`) REFERENCES `vendor` (`VendorId`);

--
-- Constraints for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD CONSTRAINT `SubCategory_CatId_id_165293ca_fk_Category_CatId` FOREIGN KEY (`CatId_id`) REFERENCES `category` (`CatId`);

--
-- Constraints for table `subsubcategory`
--
ALTER TABLE `subsubcategory`
  ADD CONSTRAINT `SubSubCategory_SubCatId_id_62789346_fk_SubCategory_SubCatId` FOREIGN KEY (`SubCatId_id`) REFERENCES `subcategory` (`SubCatId`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_AreaId_id_b4ede9b1_fk_Area_AreaId` FOREIGN KEY (`AreaId_id`) REFERENCES `area` (`AreaId`),
  ADD CONSTRAINT `user_RoleId_id_e40ba351_fk_Role_RoleId` FOREIGN KEY (`RoleId_id`) REFERENCES `role` (`RoleId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
