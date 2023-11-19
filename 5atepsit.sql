-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 17:40
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `clienti_martucci_nicolo`
--

CREATE TABLE `clienti_martucci_nicolo` (
  `id` int(250) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `pos_lav` varchar(30) NOT NULL,
  `data_ass` date NOT NULL,
  `data_nasc` date DEFAULT NULL,
  `luogo_nasc` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `clienti_martucci_nicolo`
--

INSERT INTO `clienti_martucci_nicolo` (`id`, `nome`, `cognome`, `pos_lav`, `data_ass`, `data_nasc`, `luogo_nasc`) VALUES
(0, 'nicolo', 'martucci', 'manager', '2022-07-07', '2005-04-02', 'carpi'),
(0, 'harman', 'singh', 'segretario', '2022-08-09', '2005-10-07', 'carpi'),
(0, 'erika', 'boccadoro', 'psicologa', '2021-07-09', '2005-10-27', 'carpi');

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_lavoro_martucci_nicolo`
--

CREATE TABLE `zona_lavoro_martucci_nicolo` (
  `id` int(250) NOT NULL,
  `nome_zona` varchar(30) NOT NULL,
  `numero_clienti` int(250) NOT NULL,
  `id_dipendente` varchar(30) NOT NULL,
  `numero_dipendenti` int(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `zona_lavoro_martucci_nicolo`
--

INSERT INTO `zona_lavoro_martucci_nicolo` (`id`, `nome_zona`, `numero_clienti`, `id_dipendente`, `numero_dipendenti`) VALUES
(10, 'uffici', 10, '12w', 7),
(11, 'magazzino', 0, '12e', 15),
(12, 'sala_di_accoglienza', 50, '12d', 2);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_lavoro_martucci_nicolo`
--
ALTER TABLE `zona_lavoro_martucci_nicolo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_lavoro_martucci_nicolo`
--
ALTER TABLE `zona_lavoro_martucci_nicolo`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
