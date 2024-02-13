-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server

-- Modify column `name` in table `first_table`
ALTER TABLE `first_table` MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Modify all columns in table `first_table`
ALTER TABLE `first_table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Modify character set and collation for database `hbtn_0c_0`
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
