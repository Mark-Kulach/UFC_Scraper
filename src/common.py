# src/common.py

# === Standard Libraries ===
import os
import re
import time
import threading

# === Third-Party Libraries ===
import numpy as np
import cv2
import pytesseract
import mss
import sounddevice as sd
import psycopg2
from psycopg2 import sql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# === Google Drive API ===
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# === Mediapipe ===
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils