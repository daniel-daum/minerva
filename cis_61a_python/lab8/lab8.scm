; # 1
(define (over-or-under x y)
  (cond ((< x y) -1)
        ((= x y) 0)
        ((> x y) 1)))

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; ; expect 0


; # 2
(define (filter-lst f lst)
  (cond ((null? lst) '())                      
        ((f (car lst))                      
         (cons (car lst) (filter-lst f (cdr lst)))) 
        (else (filter-lst f (cdr lst)))))  

;;; Tests
(define (even? x) 
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


; # 3
(define (make-adder num)
  (lambda (x) (+ x num)))

;;; Tests
(define adder (make-adder 5))
(adder 8) 
; expect 13 
;

; # 4
(define (composed f g)
  (lambda (x)
    (f (g x))))

; # 5
(cons (list 1)
      (cons 2
            (cons (list 3 4)
                  (list 5))))

; #6
(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst))

; #7
define (no-repeats s)
  (let ((seen '())) 
    (define (not-seen-before? x)
      (if (member x seen)
          #f
          (begin (set! seen (cons x seen)) #t)))
    (filter not-seen-before? s)))
  
  
  
#8
(define (substitute s old new)
  (cond

    ((null? s) '())
    
    ((pair? (car s)) 
     (cons (substitute (car s) old new) (substitute (cdr s) old new)))
    
    ((equal? (car s) old) 
     (cons new (substitute (cdr s) old new)))
    
    (else 
     (cons (car s) (substitute (cdr s) old new)))))

#9
(define (sub-all s olds news)
  (cond

      ((null? olds) s)
    
    (else
     (sub-all (substitute s (car olds) (car news)) 
              (cdr olds) 
              (cdr news)))))
