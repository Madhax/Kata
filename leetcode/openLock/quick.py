class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def int_to_str(n):
            n = str(abs(n))
            zero = (4-len(n)) * '0'
            return zero+n       
        
        
        def next_n(current_lock):
            def dead_test(add_n):
                nonlocal update_lock
                idx = -(len(str(abs(add_n))))
                # print(10 ** abs(idx+1),update_lock[idx])
                lock = 10 ** abs(idx+1) * int(update_lock[idx])
                # print('before',update_lock)
                temp = lock + add_n
                temp = int_to_str(temp)
                # print('now',update_lock,'add2',add_n,'=',temp,'idx',idx)
                
                
                test_lock = update_lock[:]
                test_lock[idx] = temp[idx]
                # print('test_lock',test_lock)
                if ''.join(test_lock) in deadends:
                    return False
                update_lock = test_lock
                self.count += 1
                # print('update cl',update_lock)
                return True
            
            def add_num(idx):
                nonlocal update_lock
                n = update_lock[idx]
                t = 10 ** abs(idx+1) if n > '5' else -(10 ** abs(idx+1))
                if n == '0':
                    if update_lock == current_lock:
                        hold.append(t) #暫存其他可以動的選擇 
                        hold.append(-t)
                    return 

                ok = dead_test(t)
                if not ok:
                    if update_lock == current_lock:
                        good_move.append(t)
                        hold.append(-t)
                return 
            
            def clean_good_moves():
                nonlocal good_move
                while good_move:
                    pass_ = 0
                    for n in good_move:
                        ok = dead_test(n)
                        if ok:
                            pass_ += 1
                            good_move.remove(n)
                    if pass_ == 0:
                        break
                return
            
            #----------------function code start
            #count = 0
            update_lock = current_lock[:]
            good_move = []
            hold = []
            for i in range(-4,0):                
                add_n = add_num(i) 
            
            if update_lock != current_lock:
                clean_good_moves()
                return update_lock
            
            # print('not found good match, look for optional matches.')
            if not hold:
                return False
            
            while hold:
                add_n = hold.pop()
                ok = dead_test(add_n)
                if not ok:
                    continue  
                    
                clean_good_moves()
                
                if update_lock == current_lock:
                    return False
                return update_lock
            
        
        #---------------start from target                
        self.count = 0
        target = list(target)
        if '0000' in deadends:
            return -1
        
        while target != ['0']*4:
            target = next_n(target)
            if not target:
                return -1
        
        return self.count