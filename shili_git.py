from lei_git import Student, Admin

        
sunyt = Student('sunyt', '01', 'm', 21, 'henan')
sunyt.show_grades()
sunyt.show_infos()

chendb = Admin('chendb', '10', 'm', 20, 'jiangsu', '班会')
chendb.show_privilege()
chendb.show_grades()

yuanwz = Admin('yuanwz', '23', 'f', 19, 'haerbin', '团日活动')
yuanwz.show_privilege()
yuanwz.show_infos()
