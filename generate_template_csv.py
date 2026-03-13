import csv

COLUMNS = [
    "rashi", "month_year",
    "intro_en", "intro_kn",
    "career_en", "career_kn",
    "finance_en", "finance_kn",
    "family_en", "family_kn",
    "health_en", "health_kn",
    "growth_en", "growth_kn",
    "remedy_en", "remedy_kn",
    "conclusion_en", "conclusion_kn"
]

rows = [
    {
        "rashi": "mesha",
        "month_year": "April 2026",
        "intro_en": "April 2026 is an important month for Mesha Rashi natives. With the Sun entering Aries during this period, your personal energy, confidence, and leadership qualities become stronger. This transit brings opportunities for growth, recognition, and new beginnings. However, it also requires careful decision-making and balanced actions.",
        "intro_kn": "ಏಪ್ರಿಲ್ 2026 ತಿಂಗಳು ಮೇಷ ರಾಶಿಯವರಿಗೆ ಪ್ರಮುಖ ಸಮಯವಾಗಿರುತ್ತದೆ. ಈ ಅವಧಿಯಲ್ಲಿ ಸೂರ್ಯನು ಮೇಷ ರಾಶಿಗೆ ಪ್ರವೇಶಿಸುವುದರಿಂದ ಆತ್ಮವಿಶ್ವಾಸ, ನಾಯಕತ್ವ ಮತ್ತು ವ್ಯಕ್ತಿತ್ವದ ಶಕ್ತಿ ಹೆಚ್ಚಾಗುತ್ತದೆ. ಈ ಸಂಚಾರವು ಹೊಸ ಅವಕಾಶಗಳು, ಗೌರವ ಮತ್ತು ಬೆಳವಣಿಗೆಗೆ ಕಾರಣವಾಗಬಹುದು. ಆದರೆ ಮಹತ್ವದ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವಾಗ ಸಮತೋಲನ ಮತ್ತು ಜಾಗ್ರತೆ ಅಗತ್ಯ.",
        "career_en": "This month may bring increased visibility and recognition in your professional life. You may receive appreciation from seniors or gain opportunities to take on leadership roles. If you have been waiting for progress in your career, April can open new doors.\n\nBusiness owners may experience new opportunities through networking and bold initiatives. However, it is important to avoid impulsive decisions and conflicts with colleagues or partners. Maintaining professionalism and patience will help you achieve better results.\n\nStudents preparing for competitive exams or higher studies may feel motivated and focused during this period.",
        "career_kn": "ಈ ತಿಂಗಳು ಉದ್ಯೋಗದಲ್ಲಿ ಗುರುತಿನೊಂದಿಗೆ ಹೊಸ ಅವಕಾಶಗಳು ದೊರೆಯಬಹುದು. ಮೇಲಾಧಿಕಾರಿಗಳಿಂದ ಪ್ರಶಂಸೆ ಸಿಗಬಹುದು ಮತ್ತು ನಾಯಕತ್ವದ ಜವಾಬ್ದಾರಿಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವ ಅವಕಾಶವೂ ದೊರೆಯಬಹುದು. ನಿಮ್ಮ ವೃತ್ತಿಯಲ್ಲಿ ಬೆಳವಣಿಗೆಗಾಗಿ ಕಾಯುತ್ತಿದ್ದರೆ ಈ ತಿಂಗಳು ಹೊಸ ದಾರಿಗಳನ್ನು ತೆರೆದಿಡಬಹುದು.\n\nವ್ಯಾಪಾರಸ್ಥರಿಗೆ ಹೊಸ ಸಂಪರ್ಕಗಳು ಮತ್ತು ಧೈರ್ಯವಾದ ನಿರ್ಧಾರಗಳಿಂದ ಅವಕಾಶಗಳು ದೊರೆಯಬಹುದು. ಆದರೆ ತುರ್ತು ನಿರ್ಧಾರಗಳು ಮತ್ತು ಸಹೋದ್ಯೋಗಿಗಳೊಂದಿಗೆ ವಾದಗಳನ್ನು ತಪ್ಪಿಸಬೇಕು. ಸಹನೆ ಮತ್ತು ವೃತ್ತಿಪರ ನಡವಳಿಕೆ ಉತ್ತಮ ಫಲಿತಾಂಶಗಳನ್ನು ನೀಡುತ್ತದೆ.\n\nಸ್ಪರ್ಧಾತ್ಮಕ ಪರೀಕ್ಷೆಗಳಿಗೆ ಸಿದ್ಧತೆ ಮಾಡುತ್ತಿರುವ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಈ ಅವಧಿಯಲ್ಲಿ ಗಮನ ಮತ್ತು ಪ್ರೇರಣೆ ಹೆಚ್ಚಾಗುತ್ತದೆ.",
        "finance_en": "Financially, the month may bring a mix of income and expenses. While new opportunities for earning may arise, expenses related to lifestyle, celebrations, or family responsibilities may also increase.\n\nIt is advisable to maintain financial discipline and avoid unnecessary spending. Long-term investments and savings planning may be beneficial during this period. Careful budgeting will help maintain stability.",
        "finance_kn": "ಹಣಕಾಸಿನ ದೃಷ್ಟಿಯಿಂದ ಈ ತಿಂಗಳು ಆದಾಯ ಮತ್ತು ಖರ್ಚಿನ ಮಿಶ್ರಣವಾಗಿರಬಹುದು. ಹೊಸ ಆದಾಯದ ಅವಕಾಶಗಳು ದೊರೆಯಬಹುದು, ಆದರೆ ಜೀವನಶೈಲಿ, ಆಚರಣೆಗಳು ಅಥವಾ ಕುಟುಂಬದ ಜವಾಬ್ದಾರಿಗಳಿಂದ ಖರ್ಚು ಹೆಚ್ಚಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ.\n\nಆದ್ದರಿಂದ ಹಣಕಾಸಿನಲ್ಲಿ ಶಿಸ್ತನ್ನು ಪಾಲಿಸಿ ಮತ್ತು ಅನಾವಶ್ಯಕ ಖರ್ಚುಗಳನ್ನು ತಪ್ಪಿಸಿ. ದೀರ್ಘಕಾಲದ ಹೂಡಿಕೆ ಮತ್ತು ಉಳಿತಾಯ ಯೋಜನೆಗಳು ಈ ಸಮಯದಲ್ಲಿ ಉತ್ತಮವಾಗಿರಬಹುದು.",
        "family_en": "Family life may remain generally supportive, but minor misunderstandings could arise due to strong opinions or impatience. Practicing calm communication and understanding will help maintain harmony at home.\n\nFor married couples, spending quality time together will strengthen the relationship. Unmarried individuals may receive new proposals or develop meaningful connections.\n\nSupport from elders and family members can provide emotional stability during this time.",
        "family_kn": "ಕುಟುಂಬ ಜೀವನ ಸಾಮಾನ್ಯವಾಗಿ ಸಹಕಾರದಿಂದ ಸಾಗಬಹುದು. ಆದರೆ ಅತಿಯಾದ ಅಭಿಪ್ರಾಯಗಳು ಅಥವಾ ಅಸಹನೆಯಿಂದ ಸಣ್ಣ ಭಿನ್ನಾಭಿಪ್ರಾಯಗಳು ಉಂಟಾಗಬಹುದು. ಶಾಂತವಾಗಿ ಮಾತನಾಡುವುದು ಮತ್ತು ಪರಸ್ಪರ ಅರ್ಥೈಸಿಕೊಳ್ಳುವುದು ಮನೆಯ ಶಾಂತಿಯನ್ನು ಕಾಪಾಡುತ್ತದೆ.\n\nವಿವಾಹಿತರಾದವರು ಒಟ್ಟಿಗೆ ಸಮಯ ಕಳೆಯುವುದರಿಂದ ಸಂಬಂಧ ಗಟ್ಟಿಯಾಗುತ್ತದೆ. ಅವಿವಾಹಿತರಿಗೆ ಹೊಸ ಪರಿಚಯಗಳು ಅಥವಾ ಸಂಬಂಧಗಳ ಅವಕಾಶಗಳು ದೊರೆಯಬಹುದು.\n\nಹಿರಿಯರು ಮತ್ತು ಕುಟುಂಬದ ಸದಸ್ಯರಿಂದ ಸಹಕಾರ ಮತ್ತು ಮನೋಬಲ ದೊರೆಯಬಹುದು.",
        "health_en": "Your energy levels may remain high during this month, but it is important to avoid overexertion. Stress, headaches, or heat-related issues may occasionally occur.\n\nMaintaining a balanced routine with proper sleep, hydration, and regular exercise will support overall health. Practicing yoga, meditation, or breathing exercises can also help maintain mental clarity and emotional balance.",
        "health_kn": "ಈ ತಿಂಗಳಲ್ಲಿ ಶಕ್ತಿ ಮತ್ತು ಉತ್ಸಾಹ ಹೆಚ್ಚಾಗಬಹುದು. ಆದರೆ ಅತಿಯಾದ ಕೆಲಸದಿಂದ ದಣಿವು, ತಲೆನೋವು ಅಥವಾ ದೇಹದ ಉಷ್ಣತೆ ಹೆಚ್ಚಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ.\n\nಸರಿಯಾದ ನಿದ್ರೆ, ನೀರು ಕುಡಿಯುವುದು ಮತ್ತು ನಿಯಮಿತ ವ್ಯಾಯಾಮ ಆರೋಗ್ಯವನ್ನು ಕಾಪಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಯೋಗ, ಧ್ಯಾನ ಮತ್ತು ಪ್ರಾಣಾಯಾಮ ಮಾನಸಿಕ ಶಾಂತಿಯನ್ನು ನೀಡುತ್ತದೆ.",
        "growth_en": "April is a powerful month for self-development and personal growth. Your confidence and determination may help you take bold steps toward your goals. This is a good time to start new projects, improve leadership skills, and build your public image.\n\nSocial interactions and networking may bring new opportunities that could benefit you in the long run.",
        "growth_kn": "ಏಪ್ರಿಲ್ ತಿಂಗಳು ಆತ್ಮವಿಕಾಸ ಮತ್ತು ವ್ಯಕ್ತಿತ್ವ ಬೆಳವಣಿಗೆಗೆ ಉತ್ತಮ ಸಮಯ. ಆತ್ಮವಿಶ್ವಾಸ ಮತ್ತು ಧೈರ್ಯದಿಂದ ನಿಮ್ಮ ಗುರಿಗಳತ್ತ ದೊಡ್ಡ ಹೆಜ್ಜೆಗಳನ್ನು ಇಡಬಹುದು.\n\nಹೊಸ ಯೋಜನೆಗಳನ್ನು ಆರಂಭಿಸಲು, ನಾಯಕತ್ವ ಕೌಶಲ್ಯವನ್ನು ಹೆಚ್ಚಿಸಲು ಮತ್ತು ಸಮಾಜದಲ್ಲಿ ನಿಮ್ಮ ಪ್ರಭಾವವನ್ನು ಹೆಚ್ಚಿಸಲು ಇದು ಉತ್ತಮ ಸಮಯ. ಹೊಸ ಪರಿಚಯಗಳು ಭವಿಷ್ಯದಲ್ಲಿ ಲಾಭಕರವಾಗಬಹುದು.",
        "remedy_en": "To strengthen positive energies during this month:\n\nOffer water to the Sun every morning and chant \"Om Suryaya Namah\" 11 times.",
        "remedy_kn": "ಈ ತಿಂಗಳಲ್ಲಿ ಶುಭಫಲಗಳನ್ನು ಹೆಚ್ಚಿಸಲು:\n\nಪ್ರತಿ ಬೆಳಗ್ಗೆ ಸೂರ್ಯನಿಗೆ ಅರ್ಘ್ಯ ನೀಡಿ. \"ಓಂ ಸೂರ್ಯಾಯ ನಮಃ\" ಮಂತ್ರವನ್ನು 11 ಬಾರಿ ಜಪಿಸಿ.",
        "conclusion_en": "April 2026 brings renewed confidence, growth, and opportunities for Mesha Rashi natives. By maintaining discipline, patience, and balanced decision-making, you can make the most of this positive period and move forward toward your goals.",
        "conclusion_kn": "ಏಪ್ರಿಲ್ 2026 ಮೇಷ ರಾಶಿಯವರಿಗೆ ಆತ್ಮವಿಶ್ವಾಸ, ಬೆಳವಣಿಗೆ ಮತ್ತು ಹೊಸ ಅವಕಾಶಗಳನ್ನು ತರುತ್ತದೆ. ಸಹನೆ, ಶಿಸ್ತು ಮತ್ತು ಸಮತೋಲನದ ನಿರ್ಧಾರಗಳಿಂದ ಈ ಸಮಯವನ್ನು ಉತ್ತಮವಾಗಿ ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಗುರಿಗಳತ್ತ ಮುಂದೆ ಸಾಗಬಹುದು.",
    },
    {
        "rashi": "vrishabha",
        "month_year": "April 2026",
        "intro_en": "April 2026 encourages Vrushabha Rashi natives to focus on inner stability, careful planning, and emotional balance. During this month, the Sun moves through the Aries sign, which may create a period of reflection and preparation before new opportunities begin to unfold.\n\nThis is a time to slow down, evaluate your goals, and strengthen your foundations for the future.",
        "intro_kn": "ಏಪ್ರಿಲ್ 2026 ವೃಷಭ ರಾಶಿಯವರಿಗೆ ಆಂತರಿಕ ಸ್ಥಿರತೆ, ಜಾಗ್ರತೆಯ ಯೋಜನೆ ಮತ್ತು ಮನಸ್ಸಿನ ಸಮತೋಲನದ ಮೇಲೆ ಗಮನಹರಿಸಲು ಸೂಚಿಸುತ್ತದೆ. ಈ ಅವಧಿಯಲ್ಲಿ ಸೂರ್ಯನು ಮೇಷ ರಾಶಿಯಲ್ಲಿ ಸಂಚರಿಸುವುದರಿಂದ ಹೊಸ ಅವಕಾಶಗಳು ಬರುವ ಮೊದಲು ಆತ್ಮಪರಿಶೀಲನೆ ಮತ್ತು ಸಿದ್ಧತೆಯ ಅವಧಿಯಾಗಿರಬಹುದು.\n\nಈ ಸಮಯದಲ್ಲಿ ನಿಮ್ಮ ಗುರಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಭವಿಷ್ಯಕ್ಕಾಗಿ ಬಲವಾದ ನೆಲೆ ನಿರ್ಮಿಸುವುದು ಉತ್ತಮ.",
        "career_en": "Professional life may require patience during this month. Work responsibilities could increase, and some tasks may take longer than expected to complete. It is important to stay focused and avoid unnecessary workplace conflicts.\n\nThis period may also help you plan future career strategies. Individuals working in finance, banking, agriculture, food industry, arts, or design-related professions may benefit from careful planning and consistent effort.\n\nBusiness owners should avoid risky investments or partnerships during this period and focus on strengthening existing operations.",
        "career_kn": "ಈ ತಿಂಗಳಲ್ಲಿ ಉದ್ಯೋಗ ಕ್ಷೇತ್ರದಲ್ಲಿ ಸಹನೆ ಅಗತ್ಯವಾಗಬಹುದು. ಕೆಲವು ಕೆಲಸಗಳು ನಿರೀಕ್ಷಿಸಿದ ಸಮಯಕ್ಕಿಂತ ಹೆಚ್ಚು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು ಮತ್ತು ಜವಾಬ್ದಾರಿಗಳು ಹೆಚ್ಚಾಗಬಹುದು. ಕಚೇರಿಯಲ್ಲಿ ಅನಗತ್ಯ ವಾದಗಳನ್ನು ತಪ್ಪಿಸಿ ಮತ್ತು ಕೆಲಸದ ಮೇಲೆ ಗಮನಹರಿಸಿ.\n\nಈ ಸಮಯ ಭವಿಷ್ಯದ ವೃತ್ತಿ ಯೋಜನೆಗಳನ್ನು ರೂಪಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು. ಹಣಕಾಸು, ಬ್ಯಾಂಕಿಂಗ್, ಕೃಷಿ, ಆಹಾರ ಉದ್ಯಮ, ಕಲೆ ಅಥವಾ ವಿನ್ಯಾಸ ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ಕೆಲಸ ಮಾಡುವವರಿಗೆ ಜಾಗ್ರತೆಯ ಪ್ರಯತ್ನಗಳಿಂದ ಲಾಭ ದೊರೆಯಬಹುದು.\n\nವ್ಯಾಪಾರಸ್ಥರು ಈ ಅವಧಿಯಲ್ಲಿ ಅಪಾಯಕರ ಹೂಡಿಕೆಗಳನ್ನು ತಪ್ಪಿಸಿ ಮತ್ತು ಈಗಿರುವ ವ್ಯವಹಾರವನ್ನು ಬಲಪಡಿಸಲು ಗಮನ ಕೊಡಬೇಕು.",
        "finance_en": "Financially, this month encourages caution and discipline. Unexpected expenses related to family matters or health may arise. Therefore, it is advisable to maintain a clear budget and avoid unnecessary spending.\n\nThis is a suitable time to focus on savings, financial planning, and long-term stability rather than quick profits. Careful financial decisions taken now can bring benefits in the coming months.",
        "finance_kn": "ಹಣಕಾಸಿನ ದೃಷ್ಟಿಯಿಂದ ಈ ತಿಂಗಳು ಜಾಗ್ರತೆ ಮತ್ತು ಶಿಸ್ತನ್ನು ಸೂಚಿಸುತ್ತದೆ. ಕುಟುಂಬ ಅಥವಾ ಆರೋಗ್ಯಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಅಚಾನಕ್ ಖರ್ಚುಗಳು ಸಂಭವಿಸಬಹುದು. ಆದ್ದರಿಂದ ಸ್ಪಷ್ಟವಾದ ಬಜೆಟ್ ಯೋಜನೆ ಮಾಡುವುದು ಉತ್ತಮ.\n\nತ್ವರಿತ ಲಾಭಕ್ಕಿಂತ ಉಳಿತಾಯ ಮತ್ತು ದೀರ್ಘಕಾಲದ ಹಣಕಾಸು ಯೋಜನೆಗಳಿಗೆ ಆದ್ಯತೆ ನೀಡುವುದು ಉತ್ತಮ. ಈಗ ತೆಗೆದುಕೊಳ್ಳುವ ಜಾಣ್ಮೆಯ ನಿರ್ಧಾರಗಳು ಮುಂದಿನ ತಿಂಗಳಲ್ಲಿ ಲಾಭ ತರಬಹುದು.",
        "family_en": "Family life may require patience and understanding. You may prefer spending more time in a calm environment rather than social gatherings. Minor misunderstandings may arise due to communication gaps.\n\nMaintaining open conversations and emotional balance will help strengthen relationships. Support from close family members and trusted friends may provide comfort and guidance during this period.",
        "family_kn": "ಕುಟುಂಬ ಜೀವನದಲ್ಲಿ ಸಹನೆ ಮತ್ತು ಪರಸ್ಪರ ಅರ್ಥೈಸಿಕೊಳ್ಳುವಿಕೆ ಅಗತ್ಯವಾಗಬಹುದು. ಈ ಸಮಯದಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಶಾಂತ ವಾತಾವರಣದಲ್ಲಿ ಸಮಯ ಕಳೆಯಲು ಇಷ್ಟಪಡಬಹುದು.\n\nಸಂವಹನದ ಕೊರತೆಯಿಂದ ಸಣ್ಣ ಭಿನ್ನಾಭಿಪ್ರಾಯಗಳು ಉಂಟಾಗಬಹುದು. ತೆರೆಯಾಗಿ ಮಾತನಾಡುವುದು ಮತ್ತು ಮನಸ್ಸಿನ ಸಮತೋಲನ ಕಾಪಾಡಿಕೊಳ್ಳುವುದು ಸಂಬಂಧಗಳನ್ನು ಗಟ್ಟಿಗೊಳಿಸುತ್ತದೆ. ಕುಟುಂಬದವರು ಮತ್ತು ಸ್ನೇಹಿತರಿಂದ ಸಹಕಾರ ದೊರೆಯಬಹುದು.",
        "health_en": "Health may generally remain stable, but stress and fatigue may occasionally arise due to work pressure or overthinking. Maintaining a healthy routine with balanced diet, proper sleep, and physical activity will be beneficial.\n\nSpending time in nature, practicing meditation, and avoiding excessive worry will help maintain emotional well-being.",
        "health_kn": "ಆರೋಗ್ಯ ಸಾಮಾನ್ಯವಾಗಿ ಸ್ಥಿರವಾಗಿರಬಹುದು. ಆದರೆ ಕೆಲಸದ ಒತ್ತಡ ಅಥವಾ ಹೆಚ್ಚು ಯೋಚನೆಯಿಂದ ದಣಿವು ಮತ್ತು ಮಾನಸಿಕ ಒತ್ತಡ ಉಂಟಾಗಬಹುದು.\n\nಸರಿಯಾದ ಆಹಾರ, ಸಮರ್ಪಕ ನಿದ್ರೆ ಮತ್ತು ನಿಯಮಿತ ವ್ಯಾಯಾಮ ಆರೋಗ್ಯವನ್ನು ಕಾಪಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಪ್ರಕೃತಿಯಲ್ಲಿ ಸಮಯ ಕಳೆಯುವುದು ಮತ್ತು ಧ್ಯಾನ ಮಾಡುವುದು ಮನಶಾಂತಿಯನ್ನು ನೀಡುತ್ತದೆ.",
        "growth_en": "April may encourage Vrushabha Rashi individuals to reflect on their life direction and make thoughtful decisions. This period is beneficial for spiritual learning, self-improvement, and developing inner strength.\n\nYou may feel inclined toward meditation, devotional practices, or gaining deeper knowledge about life and spirituality.",
        "growth_kn": "ಏಪ್ರಿಲ್ ತಿಂಗಳು ವೃಷಭ ರಾಶಿಯವರಿಗೆ ಜೀವನದ ದಿಕ್ಕನ್ನು ಪರಿಶೀಲಿಸಲು ಮತ್ತು ಜಾಣ್ಮೆಯ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಪ್ರೇರೇಪಿಸಬಹುದು. ಆತ್ಮವಿಕಾಸ ಮತ್ತು ಆಧ್ಯಾತ್ಮಿಕ ಅಭ್ಯಾಸಗಳಿಗೆ ಇದು ಉತ್ತಮ ಸಮಯ.\n\nಧ್ಯಾನ, ಭಕ್ತಿ ಮತ್ತು ಆಧ್ಯಾತ್ಮಿಕ ಜ್ಞಾನಗಳತ್ತ ಆಸಕ್ತಿ ಹೆಚ್ಚಾಗಬಹುದು.",
        "remedy_en": "To maintain positivity and inner peace during this month:\n\nChant \"Om Namah Shivaya\" daily and offer prayers to Lord Shiva, especially on Mondays.",
        "remedy_kn": "ಈ ತಿಂಗಳಲ್ಲಿ ಮನಶಾಂತಿ ಮತ್ತು ಶುಭಫಲಕ್ಕಾಗಿ:\n\nಪ್ರತಿದಿನ \"ಓಂ ನಮಃ ಶಿವಾಯ\" ಮಂತ್ರವನ್ನು ಜಪಿಸಿ ಮತ್ತು ವಿಶೇಷವಾಗಿ ಸೋಮವಾರ ಶಿವನನ್ನು ಪೂಜಿಸಿ.",
        "conclusion_en": "April 2026 may be a reflective and preparatory period for Vrushabha Rashi natives. By maintaining patience, financial discipline, and emotional balance, you can build a strong foundation for future opportunities.",
        "conclusion_kn": "ಏಪ್ರಿಲ್ 2026 ವೃಷಭ ರಾಶಿಯವರಿಗೆ ಆತ್ಮಪರಿಶೀಲನೆ ಮತ್ತು ಸಿದ್ಧತೆಯ ಸಮಯವಾಗಿರಬಹುದು. ಸಹನೆ, ಹಣಕಾಸಿನ ಶಿಸ್ತು ಮತ್ತು ಮನಸ್ಸಿನ ಸಮತೋಲನವನ್ನು ಕಾಪಾಡಿಕೊಂಡರೆ ಮುಂದಿನ ಅವಕಾಶಗಳಿಗೆ ಬಲವಾದ ನೆಲೆ ನಿರ್ಮಿಸಬಹುದು.",
    }
]

with open("rashis.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

print("rashis.csv created successfully with Mesha and Vrishabha data.")
