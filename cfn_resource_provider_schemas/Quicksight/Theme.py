SCHEMA = {
  "typeName" : "AWS::QuickSight::Theme",
  "description" : "Definition of the AWS::QuickSight::Theme Resource Type.",
  "definitions" : {
    "BorderStyle" : {
      "type" : "object",
      "description" : "<p>The display options for tile borders for visuals.</p>",
      "properties" : {
        "Show" : {
          "type" : "boolean",
          "default" : None,
          "description" : "<p>The option to enable display of borders for visuals.</p>"
        }
      },
      "additionalProperties" : False
    },
    "DataColorPalette" : {
      "type" : "object",
      "description" : "<p>The theme colors that are used for data colors in charts. The colors description is a\n            hexadecimal color code that consists of six alphanumerical characters, prefixed with\n                <code>#</code>, for example #37BFF5. </p>",
      "properties" : {
        "Colors" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^#[A-F0-9]{6}$"
          },
          "maxItems" : 100,
          "minItems" : 0,
          "description" : "<p>The hexadecimal codes for the colors.</p>"
        },
        "MinMaxGradient" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^#[A-F0-9]{6}$"
          },
          "maxItems" : 100,
          "minItems" : 0,
          "description" : "<p>The minimum and maximum hexadecimal codes that describe a color gradient. </p>"
        },
        "EmptyFillColor" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The hexadecimal code of a color that applies to charts where a lack of data is\n            highlighted.</p>"
        }
      },
      "additionalProperties" : False
    },
    "Font" : {
      "type" : "object",
      "properties" : {
        "FontFamily" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "GutterStyle" : {
      "type" : "object",
      "description" : "<p>The display options for gutter spacing between tiles on a sheet.</p>",
      "properties" : {
        "Show" : {
          "type" : "boolean",
          "default" : None,
          "description" : "<p>This Boolean value controls whether to display a gutter space between sheet tiles.\n        </p>"
        }
      },
      "additionalProperties" : False
    },
    "MarginStyle" : {
      "type" : "object",
      "description" : "<p>The display options for margins around the outside edge of sheets.</p>",
      "properties" : {
        "Show" : {
          "type" : "boolean",
          "default" : None,
          "description" : "<p>This Boolean value controls whether to display sheet margins.</p>"
        }
      },
      "additionalProperties" : False
    },
    "ResourcePermission" : {
      "type" : "object",
      "description" : "<p>Permission for the resource.</p>",
      "properties" : {
        "Principal" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>The Amazon Resource Name (ARN) of the principal. This can be one of the\n            following:</p>\n         <ul>\n            <li>\n               <p>The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.)</p>\n            </li>\n            <li>\n               <p>The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)</p>\n            </li>\n            <li>\n               <p>The ARN of an Amazon Web Services account root: This is an IAM ARN rather than a QuickSight\n                    ARN. Use this option only to share resources (templates) across Amazon Web Services accounts.\n                    (This is less common.) </p>\n            </li>\n         </ul>"
        },
        "Actions" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          },
          "maxItems" : 20,
          "minItems" : 1,
          "description" : "<p>The IAM action to grant or revoke permissions on.</p>"
        }
      },
      "required" : [ "Actions", "Principal" ],
      "additionalProperties" : False
    },
    "ResourceStatus" : {
      "type" : "string",
      "enum" : [ "CREATION_IN_PROGRESS", "CREATION_SUCCESSFUL", "CREATION_FAILED", "UPDATE_IN_PROGRESS", "UPDATE_SUCCESSFUL", "UPDATE_FAILED", "DELETED" ]
    },
    "SheetStyle" : {
      "type" : "object",
      "description" : "<p>The theme display options for sheets. </p>",
      "properties" : {
        "Tile" : {
          "$ref" : "#/definitions/TileStyle"
        },
        "TileLayout" : {
          "$ref" : "#/definitions/TileLayoutStyle"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "description" : "<p>The key or keys of the key-value pairs for the resource tag or tags assigned to the\n            resource.</p>",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>Tag key.</p>"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>Tag value.</p>"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "ThemeConfiguration" : {
      "type" : "object",
      "description" : "<p>The theme configuration. This configuration contains all of the display properties for\n            a theme.</p>",
      "properties" : {
        "DataColorPalette" : {
          "$ref" : "#/definitions/DataColorPalette"
        },
        "UIColorPalette" : {
          "$ref" : "#/definitions/UIColorPalette"
        },
        "Sheet" : {
          "$ref" : "#/definitions/SheetStyle"
        },
        "Typography" : {
          "$ref" : "#/definitions/Typography"
        }
      },
      "additionalProperties" : False
    },
    "ThemeError" : {
      "type" : "object",
      "description" : "<p>Theme error.</p>",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/ThemeErrorType"
        },
        "Message" : {
          "type" : "string",
          "pattern" : "\\S",
          "description" : "<p>The error message.</p>"
        }
      },
      "additionalProperties" : False
    },
    "ThemeErrorType" : {
      "type" : "string",
      "enum" : [ "INTERNAL_FAILURE" ]
    },
    "ThemeType" : {
      "type" : "string",
      "enum" : [ "QUICKSIGHT", "CUSTOM", "ALL" ]
    },
    "ThemeVersion" : {
      "type" : "object",
      "description" : "<p>A version of a theme.</p>",
      "properties" : {
        "VersionNumber" : {
          "type" : "number",
          "minimum" : 1,
          "description" : "<p>The version number of the theme.</p>"
        },
        "Arn" : {
          "type" : "string",
          "description" : "<p>The Amazon Resource Name (ARN) of the resource.</p>"
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 512,
          "minLength" : 1,
          "description" : "<p>The description of the theme.</p>"
        },
        "BaseThemeId" : {
          "type" : "string",
          "maxLength" : 512,
          "minLength" : 1,
          "pattern" : "^[\\w\\-]+$",
          "description" : "<p>The Amazon QuickSight-defined ID of the theme that a custom theme inherits from. All\n            themes initially inherit from a default Amazon QuickSight theme.</p>"
        },
        "CreatedTime" : {
          "type" : "string",
          "description" : "<p>The date and time that this theme version was created.</p>",
          "format" : "date-time"
        },
        "Configuration" : {
          "$ref" : "#/definitions/ThemeConfiguration"
        },
        "Errors" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/ThemeError"
          },
          "minItems" : 1,
          "description" : "<p>Errors associated with the theme.</p>"
        },
        "Status" : {
          "$ref" : "#/definitions/ResourceStatus"
        }
      },
      "additionalProperties" : False
    },
    "TileLayoutStyle" : {
      "type" : "object",
      "description" : "<p>The display options for the layout of tiles on a sheet.</p>",
      "properties" : {
        "Gutter" : {
          "$ref" : "#/definitions/GutterStyle"
        },
        "Margin" : {
          "$ref" : "#/definitions/MarginStyle"
        }
      },
      "additionalProperties" : False
    },
    "TileStyle" : {
      "type" : "object",
      "description" : "<p>Display options related to tiles on a sheet.</p>",
      "properties" : {
        "Border" : {
          "$ref" : "#/definitions/BorderStyle"
        }
      },
      "additionalProperties" : False
    },
    "Typography" : {
      "type" : "object",
      "properties" : {
        "FontFamilies" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Font"
          },
          "maxItems" : 5,
          "minItems" : 0
        }
      },
      "additionalProperties" : False
    },
    "UIColorPalette" : {
      "type" : "object",
      "description" : "<p>The theme colors that apply to UI and to charts, excluding data colors. The colors\n            description is a hexadecimal color code that consists of six alphanumerical characters,\n            prefixed with <code>#</code>, for example #37BFF5. For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html\">Using Themes in Amazon QuickSight</a> in the <i>Amazon QuickSight User\n                Guide.</i>\n         </p>",
      "properties" : {
        "PrimaryForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The color of text and other foreground elements that appear over the primary\n            background regions, such as grid lines, borders, table banding, icons, and so on.</p>"
        },
        "PrimaryBackground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The background color that applies to visuals and other high emphasis UI.</p>"
        },
        "SecondaryForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any sheet title, sheet control text, or UI that\n            appears over the secondary background.</p>"
        },
        "SecondaryBackground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The background color that applies to the sheet background and sheet controls.</p>"
        },
        "Accent" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>This color is that applies to selected states and buttons.</p>"
        },
        "AccentForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            accent color.</p>"
        },
        "Danger" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The color that applies to error messages.</p>"
        },
        "DangerForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            error color.</p>"
        },
        "Warning" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>This color that applies to warning and informational messages.</p>"
        },
        "WarningForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            warning color.</p>"
        },
        "Success" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The color that applies to success messages, for example the check mark for a\n            successful download.</p>"
        },
        "SuccessForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            success color.</p>"
        },
        "Dimension" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The color that applies to the names of fields that are identified as\n            dimensions.</p>"
        },
        "DimensionForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            dimension color.</p>"
        },
        "Measure" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The color that applies to the names of fields that are identified as measures.</p>"
        },
        "MeasureForeground" : {
          "type" : "string",
          "pattern" : "^#[A-F0-9]{6}$",
          "description" : "<p>The foreground color that applies to any text or other elements that appear over the\n            measure color.</p>"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) of the theme.</p>"
    },
    "AwsAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "BaseThemeId" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 1,
      "pattern" : "^[\\w\\-]+$"
    },
    "Configuration" : {
      "$ref" : "#/definitions/ThemeConfiguration"
    },
    "CreatedTime" : {
      "type" : "string",
      "description" : "<p>The date and time that the theme was created.</p>",
      "format" : "date-time"
    },
    "LastUpdatedTime" : {
      "type" : "string",
      "description" : "<p>The date and time that the theme was last updated.</p>",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1
    },
    "Permissions" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ResourcePermission"
      },
      "maxItems" : 64,
      "minItems" : 1
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 1
    },
    "ThemeId" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 1,
      "pattern" : "^[\\w\\-]+$"
    },
    "Type" : {
      "$ref" : "#/definitions/ThemeType"
    },
    "Version" : {
      "$ref" : "#/definitions/ThemeVersion"
    },
    "VersionDescription" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 1
    }
  },
  "required" : [ "AwsAccountId", "ThemeId", "BaseThemeId", "Configuration", "Name" ],
  "readOnlyProperties" : [ "/properties/CreatedTime", "/properties/Version", "/properties/LastUpdatedTime", "/properties/Arn", "/properties/Type" ],
  "createOnlyProperties" : [ "/properties/AwsAccountId", "/properties/ThemeId" ],
  "primaryIdentifier" : [ "/properties/ThemeId", "/properties/AwsAccountId" ],
  "handlers" : {
    "read" : {
      "permissions" : [ "quicksight:DescribeTheme", "quicksight:DescribeThemePermissions", "quicksight:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "quicksight:DescribeTheme", "quicksight:DescribeThemePermissions", "quicksight:CreateTheme", "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "quicksight:ListThemes" ],
      "handlerSchema" : {
        "properties" : {
          "AwsAccountId" : {
            "$ref" : "resource-schema.json#/properties/AwsAccountId"
          }
        },
        "required" : [ "AwsAccountId" ]
      }
    },
    "update" : {
      "permissions" : [ "quicksight:DescribeTheme", "quicksight:DescribeThemePermissions", "quicksight:UpdateTheme", "quicksight:UpdateThemePermissions", "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "quicksight:DescribeTheme", "quicksight:DeleteTheme" ]
    }
  },
  "additionalProperties" : False,
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-quicksight",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
  }
}