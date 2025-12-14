# CacheSim Project – Team 06

## Project Title

**Simulation of Cache Memory Mapping and Replacement Algorithms**

---

## Abstract

Cache memory plays a critical role in improving system performance by reducing memory access time. This project presents a complete simulation of cache memory behavior using different **mapping techniques** and **replacement algorithms**. The implementation helps visualize cache hits, cache misses, and replacement decisions, providing a practical understanding of core **Computer Architecture** concepts through collaborative development using **Git**.

---

## Team Members and Roles

* **Gayathri M** – LFU (Least Frequently Used) Replacement Algorithm
* **Elizabeth Mathew** – Direct Mapping Technique
* **Feba Biju** – FIFO (First In First Out) Replacement Algorithm
* **Edson Edwin Ninan** – Associative Mapping Technique
* **Fathima Irfana** – LRU (Least Recently Used) Replacement Algorithm

---

## Problem Statement

To design and implement a cache memory simulator that demonstrates different cache mapping techniques and replacement algorithms, and to analyze cache performance in terms of hits and misses for a given sequence of memory accesses.

---

## Objectives

* To understand cache memory organization and working
* To implement various cache mapping techniques
* To simulate cache replacement algorithms
* To analyze cache performance using hit and miss ratios
* To practice collaborative development using Git

---

## Scope of the Project

This project focuses on:

* Single-level cache simulation
* Educational visualization of cache behavior
* Comparison of FIFO, LRU, and LFU replacement strategies

The project does not cover multi-level caches or real hardware-specific optimizations.

---

## Cache Mapping Techniques Implemented

### 1. Direct Mapping

Each block of main memory maps to exactly one cache line. This technique is simple and fast but may cause frequent conflicts.

### 2. Associative Mapping

A memory block can be placed in any cache line. It reduces conflicts but requires more complex searching.

### 3. Set-Associative Mapping

A hybrid approach where cache lines are divided into sets, combining the advantages of direct and associative mapping.

---

## Cache Replacement Algorithms Implemented

### 1. FIFO (First In First Out)

The cache block that entered first is replaced when the cache is full.

### 2. LRU (Least Recently Used)

The cache block that has not been accessed for the longest time is replaced.

### 3. LFU (Least Frequently Used)

The cache block with the lowest access frequency is replaced.

