#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
intensity_normalization.utilities.io

assortment of input/output utilities for the project

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Apr 24, 2018
"""

from glob import glob
import os

import nibabel as nib


def split_filename(filepath):
    """ split a filepath into the full path, filename, and extension (works with .nii.gz) """
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext


def open_nii(filepath):
    """ open a nifti file with nibabel and return the object """
    image = os.path.abspath(os.path.expanduser(filepath))
    obj = nib.load(image)
    return obj


def save_nii(obj, outfile, data=None, is_nii=False):
    """ save a nifti object """
    if not is_nii:
        if data is None:
            data = obj.get_fdata()
        nib.Nifti1Image(data, obj.affine, obj.header) \
            .to_filename(outfile)
    else:
        obj.to_filename(outfile)


def glob_nii(dir):
    """ return a sorted list of nifti files for a given directory """
    fns = sorted(glob(os.path.join(dir, '*.nii*')))
    return fns


def get_mask_fns(mask_dir, input_files):
    """ Select masks matching the input file for each input img
    """
    mask_files = []
    for input_fn in input_files:
        path, base, ext = split_filename(input_fn)
        underscore_split = base.split("_")
        sub_str = underscore_split[0]
        dash_split = sub_str.split("-")
        sub_num = dash_split[1]
        mask_pattern = f'rsub-{sub_num}_*-label.nii'
        possible_masks = glob(os.path.join(mask_dir, mask_pattern))
        mask_fn = possible_masks[0]
        mask_files.append(mask_fn)

        print(f"sub_num: {sub_num}")
        print(f"possible masks: {mask_files} ")
        print(f"selected mask: {mask_fn} ")
        print("--------------")

    print(f"total mask files found {mask_files}")
    mask_files = sorted(mask_files)
    return sorted(mask_files)
