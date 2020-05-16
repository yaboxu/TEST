from lei_git import Student, Admin

        
sunyt = Student('sunyt', '01', 'm', 21, 'henan')
sunyt.show_infos()
sunyt.show_grades()

chendb = Admin('chendb', '10', 'm', 20, 'jiangsu', '班会')
chendb.show_infos()
chendb.show_grades()
chendb.show_privilege()

yuanwz = Admin('yuanwz', '23', 'f', 19, 'haerbin', '团日活动')
yuanwz.show_infos()
yuanwz.show_grades()
yuanwz.show_privilege()
