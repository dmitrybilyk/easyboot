package com.learn.easyboot.models;

import lombok.Builder;
import lombok.Data;

import java.io.Serializable;

@Data
@Builder
public class Human implements Serializable {
    private String name;
}