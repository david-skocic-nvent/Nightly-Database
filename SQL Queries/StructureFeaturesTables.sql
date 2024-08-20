USE DW_P360;

DROP TABLE Structure_Feature_Langs;
DROP TABLE Structure_Feature_Preset_Values;
DROP TABLE Structure_Features;

CREATE TABLE Structure_Features (
    [Identifier] VARCHAR(30) PRIMARY KEY,
    [StructureReference] VARCHAR(15),
    [Modified] DATETIME,
    [NameInKeyLanguage] VARCHAR(120),
    [DataType] VARCHAR(30),
    [Purpose] VARCHAR(120),
    [Unit] VARCHAR(40),
    [Annotation] VARCHAR(30),

    FOREIGN KEY ([Unit])
    REFERENCES Units([Code])
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Feature_Langs (
        [StructureFeatureIdentifier] VARCHAR(30),
        [Language] VARCHAR(10),
        [Description] VARCHAR(120),

        FOREIGN KEY (StructureFeatureIdentifier)
        REFERENCES Structure_Features([Identifier])
        ON DELETE CASCADE
);

CREATE TABLE Structure_Feature_Preset_Values (
        [StructureFeatureIdentifier] VARCHAR(30),
        [StructureValueProxy] VARCHAR(150),
        [Identifier] VARCHAR(30),
        [DisplayOrder] INT,
        [AssetId] VARCHAR(60),

        FOREIGN KEY (StructureFeatureIdentifier)
        REFERENCES Structure_Features([Identifier])
        ON DELETE CASCADE
);