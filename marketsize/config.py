from typing import Dict

COUNTRY: str = 'US'
PRODUCT_CODE_FILEPATH: str = 'foiclass.txt'
START_DATE: str = '2016-01-01'
END_DATE: str = '2018-12-31'

DOLLARS_PER_FILING: int = 1_000_000
HYPOTHETICAL_PROPORTION_OF_MARKET: float = 0.05

COST_PER_DEV_FULLY_LOADED = 200_000

PRODUCT_CODE_WEIGHTS: Dict[str, float] = {
    'LLZ': 1.0,  # System, Image Processing, Radiological
    'IYN': 0.5,  # System, Imaging, Pulsed Doppler, Ultrasonic
    'JAK': 0.5,  # System, X-Ray, Tomography, Computed
    'IYE': 0.1,  # Accelerator, Linear, Medical
    'LNH': 0.5,  # System, Nuclear Magnetic Resonance Imaging
    'NAY': 0.2,  # System, Surgical, Computer Controlled Instrument
    'DQK': 0.5,  # Computer, Diagnostic, Programmable
    'MWI': 0.2,  # Monitor, Physiological, Patient (Without Arrhythmia Detection Or Alarms)
    'MQB': 0.2,  # Solid State X-Ray Imager (Flat Panel/Digital Imager)
    'DXN': 0.1,  # System, Measurement, Blood-Pressure, Non-Invasive
    'IYO': 0.5,  # System, Imaging, Pulsed Echo, Ultrasonic
    'KPS': 0.5,  # System, Tomography, Computed, Emission
    'DQA': 0.1,  # Oximeter
    'IZL': 0.5,  # System, X-Ray, Mobile
    'MHX': 0.2,  # Monitor, Physiological, Patient(With Arrhythmia Detection Or Alarms)
}
