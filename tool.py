"""
أداة فحص قوة كلمة المرور
==========================
تقوم هذه الأداة بتحليل كلمة المرور وفق عدة معايير أمنية،
وتعطي تقييمًا نهائيًا (ضعيفة / متوسطة / جيدة / قوية جدًا)
مع ملاحظات تفصيلية لتحسينها.
"""

import re
import getpass
from dataclasses import dataclass, field


# قائمة مختصرة بأشهر كلمات المرور الشائعة (يمكن توسيعها أو تحميلها من ملف)
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "qwerty",
    "abc123", "111111", "123123", "letmein", "admin", "welcome",
}

SPECIAL_CHARS_PATTERN = r"[@#$%^&*+=!\-_.?/\\|~`{}\[\]:;\"'<>,()]"


@dataclass
class PasswordCheckResult:
    """نتيجة فحص كلمة المرور."""
    score: int
    max_score: int
    label: str
    issues: list = field(default_factory=list)

    def __str__(self) -> str:
        report = [f"التقييم: {self.label} ({self.score}/{self.max_score})"]
        if self.issues:
            report.append("ملاحظات لتحسين كلمة المرور:")
            report.extend(f"  - {issue}" for issue in self.issues)
        else:
            report.append("لا توجد ملاحظات، كلمة المرور ممتازة!")
        return "\n".join(report)


def check_password_strength(password: str) -> PasswordCheckResult:
    """
    يفحص قوة كلمة المرور ويعيد نتيجة مفصّلة تتضمن نقاط التقييم
    وقائمة بالمشاكل المكتشفة (إن وُجدت).

    المعايير المعتمدة:
        1. الطول (8 أحرف على الأقل، ويُفضّل 12+)
        2. وجود أحرف صغيرة وكبيرة
        3. وجود أرقام
        4. وجود رموز خاصة
        5. عدم كونها من كلمات المرور الشائعة
        6. عدم تكرار نفس الحرف بشكل مفرط
    """
    issues: list[str] = []
    score = 0
    max_score = 6

    if not password:
        return PasswordCheckResult(0, max_score, "غير صالحة", ["كلمة المرور فارغة."])

    # 1. الطول
    if len(password) < 8:
        issues.append("يجب أن تحتوي على 8 أحرف على الأقل.")
    elif len(password) < 12:
        score += 1
        issues.append("يُفضّل استخدام 12 حرفًا أو أكثر لأمان أعلى.")
    else:
        score += 2

    # 2. أحرف صغيرة وكبيرة
    has_lower = re.search(r"[a-z]", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    if has_lower and has_upper:
        score += 1
    else:
        issues.append("أضف مزيجًا من الأحرف الكبيرة والصغيرة (A-Z, a-z).")

    # 3. أرقام
    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("أضف رقمًا واحدًا على الأقل (0-9).")

    # 4. رموز خاصة
    if re.search(SPECIAL_CHARS_PATTERN, password):
        score += 1
    else:
        issues.append("أضف رمزًا خاصًا واحدًا على الأقل (مثل @ # $ % ^ & *).")

    # 5. كلمة مرور شائعة
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        issues.append("هذه كلمة مرور شائعة جدًا وسهلة التخمين، تجنّبها تمامًا.")

    # 6. تكرار مفرط لنفس الحرف (مثل aaaa1111)
    if re.search(r"(.)\1{3,}", password):
        issues.append("تجنّب تكرار نفس الحرف أكثر من 3 مرات متتالية.")
    elif score > 0:
        score += 1

    score = max(0, min(score, max_score))

    if score <= 1:
        label = "ضعيفة"
    elif score <= 3:
        label = "متوسطة"
    elif score <= 5:
        label = "جيدة"
    else:
        label = "قوية جدًا"

    return PasswordCheckResult(score, max_score, label, issues)


def main() -> None:
    """نقطة الدخول الرئيسية للبرنامج."""
    try:
        # getpass تُخفي كلمة المرور أثناء الكتابة (أكثر أمانًا من input)
        password = getpass.getpass("أدخل كلمة المرور للفحص: ")
    except Exception:
        # في حال تعذّر استخدام getpass (بعض البيئات)، نستخدم input كبديل
        password = input("أدخل كلمة المرور للفحص: ")

    result = check_password_strength(password)
    print()
    print(result)


if __name__ == "__main__":
    main()