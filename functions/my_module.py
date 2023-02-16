def full_name(f_name, l_name, m_name=None):
    if m_name:
        return (f'{f_name} {m_name} {l_name}')
    else:
        return(f'{f_name} {l_name}')