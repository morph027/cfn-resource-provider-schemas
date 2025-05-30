SCHEMA = {
  "typeName" : "AWS::DataBrew::Recipe",
  "description" : "Resource schema for AWS::DataBrew::Recipe.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-databrew.git",
  "properties" : {
    "Description" : {
      "description" : "Description of the recipe",
      "minLength" : 0,
      "maxLength" : 1024,
      "type" : "string"
    },
    "Name" : {
      "description" : "Recipe name",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Steps" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "type" : "object",
        "$ref" : "#/definitions/RecipeStep"
      }
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "SecondaryInput" : {
      "description" : "Secondary input",
      "type" : "object",
      "properties" : {
        "S3InputDefinition" : {
          "$ref" : "#/definitions/S3Location"
        },
        "DataCatalogInputDefinition" : {
          "$ref" : "#/definitions/DataCatalogInputDefinition"
        }
      },
      "oneOf" : [ {
        "required" : [ "S3InputDefinition" ]
      }, {
        "required" : [ "DataCatalogInputDefinition" ]
      } ],
      "additionalProperties" : False
    },
    "S3Location" : {
      "description" : "Input location",
      "type" : "object",
      "properties" : {
        "Bucket" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Bucket" ]
    },
    "DataCatalogInputDefinition" : {
      "type" : "object",
      "properties" : {
        "CatalogId" : {
          "description" : "Catalog id",
          "type" : "string"
        },
        "DatabaseName" : {
          "description" : "Database name",
          "type" : "string"
        },
        "TableName" : {
          "description" : "Table name",
          "type" : "string"
        },
        "TempDirectory" : {
          "$ref" : "#/definitions/S3Location"
        }
      },
      "additionalProperties" : False
    },
    "RecipeStep" : {
      "type" : "object",
      "properties" : {
        "Action" : {
          "$ref" : "#/definitions/Action"
        },
        "ConditionExpressions" : {
          "description" : "Condition expressions applied to the step action",
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "$ref" : "#/definitions/ConditionExpression"
          }
        }
      },
      "additionalProperties" : False,
      "required" : [ "Action" ]
    },
    "Action" : {
      "type" : "object",
      "properties" : {
        "Operation" : {
          "description" : "Step action operation",
          "type" : "string"
        },
        "Parameters" : {
          "anyOf" : [ {
            "$ref" : "#/definitions/RecipeParameters"
          }, {
            "$ref" : "#/definitions/ParameterMap"
          } ]
        }
      },
      "additionalProperties" : False,
      "required" : [ "Operation" ]
    },
    "ConditionExpression" : {
      "description" : "Condition expressions applied to the step action",
      "type" : "object",
      "properties" : {
        "Condition" : {
          "description" : "Input condition to be applied to the target column",
          "type" : "string"
        },
        "Value" : {
          "description" : "Value of the condition",
          "type" : "string"
        },
        "TargetColumn" : {
          "description" : "Name of the target column",
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Condition", "TargetColumn" ]
    },
    "RecipeParameters" : {
      "additionalProperties" : False,
      "properties" : {
        "AggregateFunction" : {
          "type" : "string"
        },
        "Base" : {
          "type" : "string"
        },
        "CaseStatement" : {
          "type" : "string"
        },
        "CategoryMap" : {
          "type" : "string"
        },
        "CharsToRemove" : {
          "type" : "string"
        },
        "CollapseConsecutiveWhitespace" : {
          "type" : "string"
        },
        "ColumnDataType" : {
          "type" : "string"
        },
        "ColumnRange" : {
          "type" : "string"
        },
        "Count" : {
          "type" : "string"
        },
        "CustomCharacters" : {
          "type" : "string"
        },
        "CustomStopWords" : {
          "type" : "string"
        },
        "CustomValue" : {
          "type" : "string"
        },
        "DatasetsColumns" : {
          "type" : "string"
        },
        "DateAddValue" : {
          "type" : "string"
        },
        "DateTimeFormat" : {
          "type" : "string"
        },
        "DateTimeParameters" : {
          "type" : "string"
        },
        "DeleteOtherRows" : {
          "type" : "string"
        },
        "Delimiter" : {
          "type" : "string"
        },
        "EndPattern" : {
          "type" : "string"
        },
        "EndPosition" : {
          "type" : "string"
        },
        "EndValue" : {
          "type" : "string"
        },
        "ExpandContractions" : {
          "type" : "string"
        },
        "Exponent" : {
          "type" : "string"
        },
        "FalseString" : {
          "type" : "string"
        },
        "GroupByAggFunctionOptions" : {
          "type" : "string"
        },
        "GroupByColumns" : {
          "type" : "string"
        },
        "HiddenColumns" : {
          "type" : "string"
        },
        "IgnoreCase" : {
          "type" : "string"
        },
        "IncludeInSplit" : {
          "type" : "string"
        },
        "Interval" : {
          "type" : "string"
        },
        "IsText" : {
          "type" : "string"
        },
        "JoinKeys" : {
          "type" : "string"
        },
        "JoinType" : {
          "type" : "string"
        },
        "LeftColumns" : {
          "type" : "string"
        },
        "Limit" : {
          "type" : "string"
        },
        "LowerBound" : {
          "type" : "string"
        },
        "MapType" : {
          "type" : "string"
        },
        "ModeType" : {
          "type" : "string"
        },
        "MultiLine" : {
          "type" : "boolean"
        },
        "NumRows" : {
          "type" : "string"
        },
        "NumRowsAfter" : {
          "type" : "string"
        },
        "NumRowsBefore" : {
          "type" : "string"
        },
        "OrderByColumn" : {
          "type" : "string"
        },
        "OrderByColumns" : {
          "type" : "string"
        },
        "Other" : {
          "type" : "string"
        },
        "Pattern" : {
          "type" : "string"
        },
        "PatternOption1" : {
          "type" : "string"
        },
        "PatternOption2" : {
          "type" : "string"
        },
        "PatternOptions" : {
          "type" : "string"
        },
        "Period" : {
          "type" : "string"
        },
        "Position" : {
          "type" : "string"
        },
        "RemoveAllPunctuation" : {
          "type" : "string"
        },
        "RemoveAllQuotes" : {
          "type" : "string"
        },
        "RemoveAllWhitespace" : {
          "type" : "string"
        },
        "RemoveCustomCharacters" : {
          "type" : "string"
        },
        "RemoveCustomValue" : {
          "type" : "string"
        },
        "RemoveLeadingAndTrailingPunctuation" : {
          "type" : "string"
        },
        "RemoveLeadingAndTrailingQuotes" : {
          "type" : "string"
        },
        "RemoveLeadingAndTrailingWhitespace" : {
          "type" : "string"
        },
        "RemoveLetters" : {
          "type" : "string"
        },
        "RemoveNumbers" : {
          "type" : "string"
        },
        "RemoveSourceColumn" : {
          "type" : "string"
        },
        "RemoveSpecialCharacters" : {
          "type" : "string"
        },
        "RightColumns" : {
          "type" : "string"
        },
        "SampleSize" : {
          "type" : "string"
        },
        "SampleType" : {
          "type" : "string"
        },
        "SecondInput" : {
          "type" : "string"
        },
        "SecondaryInputs" : {
          "type" : "array",
          "insertionOrder" : True,
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/SecondaryInput"
          }
        },
        "SourceColumn" : {
          "type" : "string"
        },
        "SourceColumn1" : {
          "type" : "string"
        },
        "SourceColumn2" : {
          "type" : "string"
        },
        "SourceColumns" : {
          "type" : "string"
        },
        "StartColumnIndex" : {
          "type" : "string"
        },
        "StartPattern" : {
          "type" : "string"
        },
        "StartPosition" : {
          "type" : "string"
        },
        "StartValue" : {
          "type" : "string"
        },
        "StemmingMode" : {
          "type" : "string"
        },
        "StepCount" : {
          "type" : "string"
        },
        "StepIndex" : {
          "type" : "string"
        },
        "StopWordsMode" : {
          "type" : "string"
        },
        "Strategy" : {
          "type" : "string"
        },
        "SheetNames" : {
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "type" : "string"
          },
          "minItems" : 1,
          "maxItems" : 1
        },
        "SheetIndexes" : {
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "type" : "integer"
          },
          "minItems" : 1,
          "maxItems" : 1
        },
        "TargetColumn" : {
          "type" : "string"
        },
        "TargetColumnNames" : {
          "type" : "string"
        },
        "TargetDateFormat" : {
          "type" : "string"
        },
        "TargetIndex" : {
          "type" : "string"
        },
        "TimeZone" : {
          "type" : "string"
        },
        "TokenizerPattern" : {
          "type" : "string"
        },
        "TrueString" : {
          "type" : "string"
        },
        "UdfLang" : {
          "type" : "string"
        },
        "Units" : {
          "type" : "string"
        },
        "UnpivotColumn" : {
          "type" : "string"
        },
        "UpperBound" : {
          "type" : "string"
        },
        "UseNewDataFrame" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        },
        "Value1" : {
          "type" : "string"
        },
        "Value2" : {
          "type" : "string"
        },
        "ValueColumn" : {
          "type" : "string"
        },
        "ViewFrame" : {
          "type" : "string"
        },
        "Input" : {
          "description" : "Input",
          "type" : "object",
          "properties" : {
            "S3InputDefinition" : {
              "$ref" : "#/definitions/S3Location"
            },
            "DataCatalogInputDefinition" : {
              "$ref" : "#/definitions/DataCatalogInputDefinition"
            }
          },
          "oneOf" : [ {
            "required" : [ "S3InputDefinition" ]
          }, {
            "required" : [ "DataCatalogInputDefinition" ]
          } ],
          "additionalProperties" : False
        }
      }
    },
    "ParameterMap" : {
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "^[A-Za-z0-9]{1,128}$" : {
          "type" : "string"
        }
      }
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Value", "Key" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Steps" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "databrew:TagResource", "databrew:UntagResource", "databrew:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "databrew:CreateRecipe", "databrew:DescribeRecipe", "databrew:TagResource", "databrew:UntagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "databrew:DescribeRecipe", "databrew:ListTagsForResource", "iam:ListRoles" ]
    },
    "delete" : {
      "permissions" : [ "databrew:DeleteRecipeVersion" ]
    },
    "list" : {
      "permissions" : [ "databrew:ListRecipes", "iam:ListRoles" ]
    },
    "update" : {
      "permissions" : [ "databrew:UpdateRecipe", "databrew:TagResource", "databrew:UntagResource" ]
    }
  }
}