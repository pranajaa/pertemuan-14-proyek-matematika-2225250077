
def hitung_rata_rata(data_siswa):
    if not data_siswa:
        return 0

    total = sum(siswa["nilai"] for siswa in data_siswa)
    return total / len(data_siswa)


def nilai_tertinggi(data_siswa):
    if not data_siswa:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def nilai_terendah(data_siswa):
    if not data_siswa:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def hitung_status_kkm(data_siswa, kkm=75):
    mencapai = 0
    belum_mencapai = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            mencapai += 1
        else:
            belum_mencapai += 1

    return mencapai, belum_mencapai