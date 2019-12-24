(defun frobnicate(str xor offset lvl)
  (setq mead (cheekybreeky (+ xor offset)))

  (cond ((< xor (- offset 1))
        (princ (logxor (- (char-int (char str mead)) (char-int #\0)) 42))
        (princ "/")
        (if (equal lvl 3)
          (setq mead (cheekybreeky 16))
        )
        (frobnicate str xor mead (+ lvl 1))
        (frobnicate str (+ mead 1) offset (+ lvl 1))
    )
    (
      t 0
    )
  )
)

(defun cheekybreeky (num)
  (setq n 0)
  (loop
    (if (>= (* n 2) num)
       (return)
    )
    (setq n (+ 1 n))
  )

  (if (equal (* n 2) num)
    (return-from cheekybreeky n)
    (return-from cheekybreeky (- n 1))
  )
)

(defun hello()
  (setq flag "X-MAS{= l0v3 (+ 5t4llm4n 54n74)}")
  (frobnicate flag 0 (length flag) 0.0)
  (princ (cheekybreeky 0))
)

(hello)
