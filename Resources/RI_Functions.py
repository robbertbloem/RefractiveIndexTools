import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.CommonFunctions as CF

# REFRACTIVE INDEX

def gvd_formula_1(x, s): 
    """
    Formula 1 and 2 are the same, except that some coefficients are squared. 
    """
    if len(s) > 9:
        raise NotImplementedError("The GVD can only be calculated for the first 9 terms.")
    
    if len(s) < 9:
        _s = numpy.zeros(9)
        _s[:len(s)] = s
        s = _s

    y = (
        (6 * s[1] * s[2]**2) / (x**4 * (1 - s[2]**2 / x**2)**2) 
        + (8 * s[1] * s[2]**4) / (x**6 * (1 - s[2]**2 / x**2)**3) 
        + (6 * s[3] * s[4]**2) / (x**4 * (1 - s[4]**2 / x**2)**2) 
        + (8 * s[3] * s[4]**4) / (x**6 * (1 - s[4]**2 / x**2)**3) 
        + (6 * s[5] * s[6]**2) / (x**4 * (1 - s[6]**2 / x**2)**2) 
        + (8 * s[5] * s[6]**4) / (x**6 * (1 - s[6]**2 / x**2)**3) 
        + (6 * s[7] * s[8]**2) / (x**4 * (1 - s[8]**2 / x**2)**2) 
        + (8 * s[7] * s[8]**4) / (x**6 * (1 - s[8]**2 / x**2)**3)
    ) / (
        2 * numpy.sqrt(
            s[1] / (1 - s[2]**2 / x**2) 
            + s[3] / (1 - s[4]**2 / x**2) 
            + s[5] / (1 - s[6]**2 / x**2) 
            + s[7] / (1 - s[8]**2 / x**2) 
            + s[0] 
            + 1
        )
    ) - (
        -(2 * s[1] * s[2]**2)/(x**3 * (1 - s[2]**2 / x**2)**2) 
        - (2 * s[3] * s[4]**2)/(x**3 * (1 - s[4]**2 / x**2)**2) 
        - (2 * s[5] * s[6]**2)/(x**3 * (1 - s[6]**2 / x**2)**2) 
        - (2 * s[7] * s[8]**2)/(x**3 * (1 - s[8]**2 / x**2)**2)
    )**2 / (
        4 * (
            s[1]/(1 - s[2]**2 / x**2) 
            + s[3] / (1 - s[4]**2 / x**2) 
            + s[5] / (1 - s[6]**2 / x**2) 
            + s[7] / (1 - s[8]**2 / x**2) 
            + s[0] 
            + 1
        )**(3/2)
    )
    
    return y


def gvd_formula_3(x, s):

    """
    http://www.wolframalpha.com/input/?i=second+derivative+of+sqrt(a+%2B+b*x%5Ec+%2B+d*x%5Ee+%2B+f*x%5Eg+%2B+h*x%5Ei+%2B+j*x%5Ek+%2B+l*x%5Em+%2B+n*x%5Eo+%2Bp*x%5Eq)+with+respect+to+x
    
    """

    if len(s) < 17:
        _s = numpy.zeros(17, dtype = "float")
        _s[:len(s)] = s
        s = _s

    y = (
            s[1] * (s[2] - 1) * s[2] * x**(s[2] - 2) 
            + s[3] * (s[4] - 1) * s[4] * x**(s[4] - 2) 
            + s[5] * (s[6] - 1) * s[6] * x**(s[6] - 2) 
            + s[7] * (s[8] - 1) * s[8] * x**(s[8] - 2) 
            + s[9] * (s[10] - 1) * s[10] * x**(s[10] - 2) 
            + s[11] * (s[12] - 1) * s[12] * x**(s[12] - 2) 
            + s[13] * (s[14] - 1) * s[14] * x**(s[14] - 2) 
            + s[15] * (s[16] - 1) * s[16] * x**(s[16] - 2)
        ) / (
            2 * numpy.sqrt(
                s[0] 
                + s[1] * x**s[2] 
                + s[3] * x**s[4] 
                + s[5] * x**s[6] 
                + s[7] * x**s[8] 
                + s[9] * x**s[10] 
                + s[11] * x**s[12] 
                + s[13] * x**s[14] 
                + s[15] * x**s[16]
            )
        ) - (
            s[1] * s[2] * x**(s[2] - 1) 
            + s[3] * s[4] * x**(s[4] - 1) 
            + s[5] * s[6] * x**(s[6] - 1) 
            + s[7] * s[8] * x**(s[8] - 1) 
            + s[9] * s[10] * x**(s[10] - 1) 
            + s[11] * s[12] * x**(s[12] - 1) 
            + s[13] * s[14] * x**(s[14] - 1) 
            + s[15] * s[16] * x**(s[16] - 1)
        )**2 / (
            4 * (
                s[0] 
                + s[1] * x**s[2] 
                + s[3] * x**s[4] 
                + s[5] * x**s[6] 
                + s[7] * x**s[8] 
                + s[9] * x**s[10] 
                + s[11] * x**s[12] 
                + s[13] * x**s[14] 
                + s[15] * x**s[16]
            )**(3/2)
        )
    return y


def gvd_formula_4(x, s):
    """
    http://www.wolframalpha.com/input/?i=second+derivative+of+sqrt(a%2B+(b*x%5Ec)%2F(x%5E2-d%5Ee)+%2B+(f*x%5Eg)%2F(x%5E2-h%5Ei)+%2B+j*x%5Ek+%2B+l*x%5Em+%2B+n*x%5Eo+%2B+p*x%5Eq+)+with+respect+to+x
    
    
    """
    if len(s) < 17:
        _s = numpy.zeros(17, dtype = "float")
        _s[:len(s)] = s
        s = _s

    y = (
            (s[1] * (s[2] - 1) * s[2] * x**(s[2] - 2))/(x**2 - s[3]**s[4]) 
            + (8 * s[1] * x**(s[2] + 2))/(x**2 - s[3]**s[4])**3 
            - (2 * s[1] * s[2] * x**s[2])/(x**2 - s[3]**s[4])**2 
            - (2 * s[1] * (s[2] + 1) * x**s[2])/(x**2 - s[3]**s[4])**2 
            + (s[5] * (s[6] - 1) * s[6] * x**(s[6] - 2))/(x**2 - s[7]**s[8]) 
            + (8 * s[5] * x**(s[6] + 2))/(x**2 - s[7]**s[8])**3 
            - (2 * s[5] * s[6] * x**s[6])/(x**2 - s[7]**s[8])**2 
            - (2 * s[5] * (s[6] + 1) * x**s[6])/(x**2 - s[7]**s[8])**2 
            + s[9] * (s[10] - 1) * s[10] * x**(s[10] - 2) 
            + s[11] * (s[12] - 1) * s[12] * x**(s[12] - 2) 
            + s[13] * (s[14] - 1) * s[14] * x**(s[14] - 2) 
            + s[15] * (s[16] - 1) * s[16] * x**(s[16] - 2)
        ) / (
            2 * numpy.sqrt(
                s[0] 
                + (s[1] * x**s[2])/(x**2 - s[3]**s[4]) 
                + (s[5] * x**s[6])/(x**2 - s[7]**s[8]) 
                + s[9] * x**s[10] 
                + s[11] * x**s[12] 
                + s[13] * x**s[14] 
                + s[15] * x**s[16]
            )
        ) - (
            (s[1] * s[2] * x**(s[2] - 1))/(x**2 - s[3]**s[4]) 
            - (2 * s[1] * x**(s[2] + 1))/(x**2 - s[3]**s[4])**2 
            + (s[5] * s[6] * x**(s[6] - 1))/(x**2 - s[7]**s[8]) 
            - (2 * s[5] * x**(s[6] + 1))/(x**2 - s[7]**s[8])**2 
            + s[9] * s[10] * x**(s[10] - 1) 
            + s[11] * s[12] * x**(s[12] - 1) 
            + s[13] * s[14] * x**(s[14] - 1) 
            + s[15] * s[16] * x**(s[16] - 1)
        )**2 / (
            4 * (
                s[0] 
                + (s[1] * x**s[2])/(x**2 - s[3]**s[4]) 
                + (s[5] * x**s[6])/(x**2 - s[7]**s[8]) 
                + s[9] * x**s[10] 
                + s[11] * x**s[12] 
                + s[13] * x**s[14] 
                + s[15] * x**s[16]
            )**(3/2)
        )
    return y


    
    
def gvd_formula_5(x, s):

    """
    Formula 5 
    http://www.wolframalpha.com/input/?i=second+derivative+of+a%2B+b*x%5Ec+%2B+d*x%5Ee+%2B+f*x%5Eg+%2Bh*x%5Ei+%2B+j*x%5Ek+with+respect+to+x
    """
    
    if len(s) < 11:
        _s = numpy.zeros(11, dtype = "float")
        _s[:len(s)] = s
        s = _s  

    y = ( 
        s[1] * (s[2] - 1) * s[2] * x**(s[2] - 2) 
        + s[3] * (s[4] - 1) * s[4] * x**(s[4] - 2) 
        + s[5] * (s[6] - 1) * s[6] * x**(s[6] - 2) 
        + s[7] * (s[8] - 1) * s[8] * x**(s[8] - 2) 
        + s[9] * (s[10] - 1) * s[10] * x**(s[10] - 2)
    )
    
    return y
    
    
def gvd_formula_6(x, s):  
    """
    http://www.wolframalpha.com/input/?i=second+derivative+of+1%2Ba%2B+b%2F(c-x%5E-2)+%2B+d%2F(e-x%5E-2)+%2B+f%2F(g-x%5E-2)+%2B+h%2F(i-x%5E-2)+%2B+j%2F(k-x%5E-2)+with+respect+to+x
    """
    
    if len(s) < 11:
        _s = numpy.zeros(11, dtype = "float")
        _s[:len(s)] = s
        s = _s
        
        
    y = (
        s[1] * (
            8/((x**6) * (s[2] - 1/x**2)**3) 
            + 6/((x**4) * (s[2] - 1/x**2)**2)
        ) + s[3] * (
            8/((x**6) * (s[4] - 1/x**2)**3) 
            + 6/((x**4) * (s[4] - 1/x**2)**2)
        ) + s[5] * (
            8/((x**6) * (s[6] - 1/x**2)**3) 
            + 6/((x**4) * (s[6] - 1/x**2)**2)
        ) + s[7] * (
            8/((x**6) * (s[8] - 1/x**2)**3) 
            + 6/((x**4) * (s[8] - 1/x**2)**2)
        ) + s[9] * (
            8/((x**6) * (s[10] - 1/x**2)**3) 
            + 6/((x**4) * (s[10] - 1/x**2)**2)
        )   
    ) 
    
    return y
 
def gvd_formula_7(x, s):  
    """
    http://www.wolframalpha.com/input/?i=second+derivative+of+a+%2B+b%2F(x%5E2-0.028)%2Bc*(1%2F(x%5E2-0.028))%5E2+%2B+d*x%5E2+%2Be*x%5E4+%2Bf*x%5E6+with+respect+to+x
    """

    if len(s) < 6:
        _s = numpy.zeros(6, dtype = "float")
        _s[:len(s)] = s
        s = _s

    y = (
        s[1] * (
            (8 * x**2)/(x**2 - 0.028)**3 
            - 2/(x**2 - 0.028)**2
        ) 
        + s[2] * (
            (24 * x**2)/(x**2 - 0.028)**4 
            - 4/(x**2 - 0.028)**3
        ) 
        + 2 * s[3] 
        + 12 * s[4] * x**2 
        + 30 * s[5] * x**4   
    )
    
    return y

def reflectance(n1, n2, a_deg = [], a_range = (0,90), n_steps = -1):
    """
    It is calculated for what?
    - a_deg > a_range
    
    """

    n1 = CF.make_numpy_ndarray(n1)
    n2 = CF.make_numpy_ndarray(n2)
    a_deg = CF.make_numpy_ndarray(a_deg)

    if len(a_deg) == 0:
        if n_steps == -1:
            n_steps = int(a_range[1] - a_range[0]) + 1
            if n_steps < 5:
                n_steps = 5
        a_deg = numpy.linspace(a_range[0], a_range[1], num = n_steps)
            


    a_rad = a_deg * numpy.pi / 180
    
    N1, A = numpy.meshgrid(n1, a_rad)
    N2, A = numpy.meshgrid(n2, a_rad)
    
    # when n2 > n1, there is a critical angle. Here angles > critical angles are set to nan. 
    temp = ((N1 * numpy.sin(A)) / (N2))**2
    numpy.putmask(temp, temp >= 1, numpy.nan)
    x = numpy.sqrt(1 - temp)
    
    a = N1 * numpy.cos(A)
    b = N2 * x
    Rs = numpy.abs((a-b) / (a+b))**2
    
    a = N1 * x
    b = N2 * numpy.cos(A)
    Rp = numpy.abs((a-b) / (a+b))**2
    
    return a_deg, Rs, Rp

if __name__ == "__main__": 
    pass

    