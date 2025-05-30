SCHEMA = {
  "typeName" : "AWS::RDS::CustomDBEngineVersion",
  "description" : "Creates a custom DB engine version (CEV).",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
  },
  "definitions" : {
    "Tag" : {
      "description" : "Metadata assigned to an Amazon RDS resource consisting of a key-value pair.\n For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DatabaseInstallationFilesS3BucketName" : {
      "type" : "string",
      "description" : "The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is ``my-custom-installation-files``.",
      "minLength" : 3,
      "maxLength" : 63
    },
    "DatabaseInstallationFilesS3Prefix" : {
      "type" : "string",
      "description" : "The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is ``123456789012/cev1``. If this setting isn't specified, no prefix is assumed.",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Description" : {
      "type" : "string",
      "description" : "An optional description of your CEV.",
      "minLength" : 1,
      "maxLength" : 1000
    },
    "Engine" : {
      "type" : "string",
      "description" : "The database engine to use for your custom engine version (CEV).\n Valid values:\n  +   ``custom-oracle-ee`` \n  +   ``custom-oracle-ee-cdb``",
      "minLength" : 1,
      "maxLength" : 35
    },
    "EngineVersion" : {
      "type" : "string",
      "description" : "The name of your CEV. The name format is ``major version.customized_string``. For example, a valid CEV name is ``19.my_cev1``. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of ``Engine`` and ``EngineVersion`` is unique per customer per Region.\n  *Constraints:* Minimum length is 1. Maximum length is 60.\n  *Pattern:* ``^[a-z0-9_.-]{1,60$``}",
      "minLength" : 1,
      "maxLength" : 60
    },
    "KMSKeyId" : {
      "type" : "string",
      "description" : "The AWS KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.\n If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you don't already have a symmetric encryption KMS key in your account, follow the instructions in [Creating a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *Key Management Service Developer Guide*.\n You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Manifest" : {
      "type" : "string",
      "description" : "The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.\n The following JSON fields are valid:\n  + MediaImportTemplateVersion Version of the CEV manifest. The date is in the format YYYY-MM-DD. + databaseInstallationFileNames Ordered list of installation files for the CEV. + opatchFileNames Ordered list of OPatch installers used for the Oracle DB engine. + psuRuPatchFileNames The PSU and RU patches for this CEV. + OtherPatchFileNames The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches. \n For more information, see [Creating the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest) in the *Amazon RDS User Guide*.",
      "minLength" : 1,
      "maxLength" : 51000
    },
    "DBEngineVersionArn" : {
      "type" : "string",
      "description" : ""
    },
    "SourceCustomDbEngineVersionIdentifier" : {
      "type" : "string",
      "description" : "The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either ``Source`` or ``UseAwsProvidedLatestImage``. You can't specify a different JSON manifest when you specify ``SourceCustomDbEngineVersionIdentifier``."
    },
    "UseAwsProvidedLatestImage" : {
      "type" : "boolean",
      "description" : "Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify ``UseAwsProvidedLatestImage``, you can't also specify ``ImageId``."
    },
    "ImageId" : {
      "type" : "string",
      "description" : "A value that indicates the ID of the AMI."
    },
    "Status" : {
      "type" : "string",
      "description" : "A value that indicates the status of a custom engine version (CEV).",
      "default" : "available",
      "enum" : [ "available", "inactive", "inactive-except-restore" ]
    },
    "Tags" : {
      "description" : "A list of tags. For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide.*",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "propertyTransform" : {
    "/properties/Engine" : "$lowercase(Engine)",
    "/properties/EngineVersion" : "$lowercase(EngineVersion)",
    "/properties/KMSKeyId" : "$join([\"arn:.+?:kms:.+?:.+?:key\\/\", KMSKeyId])"
  },
  "required" : [ "Engine", "EngineVersion" ],
  "writeOnlyProperties" : [ "/properties/Manifest", "/properties/SourceCustomDbEngineVersionIdentifier", "/properties/UseAwsProvidedLatestImage" ],
  "readOnlyProperties" : [ "/properties/DBEngineVersionArn" ],
  "primaryIdentifier" : [ "/properties/Engine", "/properties/EngineVersion" ],
  "createOnlyProperties" : [ "/properties/Engine", "/properties/EngineVersion", "/properties/DatabaseInstallationFilesS3BucketName", "/properties/DatabaseInstallationFilesS3Prefix", "/properties/ImageId", "/properties/KMSKeyId", "/properties/Manifest", "/properties/SourceCustomDbEngineVersionIdentifier", "/properties/UseAwsProvidedLatestImage" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CopySnapshot", "ec2:DeleteSnapshot", "ec2:DescribeSnapshots", "kms:CreateGrant", "kms:Decrypt", "kms:DescribeKey", "kms:GenerateDataKey", "kms:ReEncrypt", "mediaimport:CreateDatabaseBinarySnapshot", "rds:AddTagsToResource", "rds:CreateCustomDBEngineVersion", "rds:DescribeDBEngineVersions", "rds:ModifyCustomDBEngineVersion", "s3:CreateBucket", "s3:GetObject", "s3:GetObjectAcl", "s3:GetObjectTagging", "s3:ListBucket", "s3:PutBucketObjectLockConfiguration", "s3:PutBucketPolicy", "s3:PutBucketVersioning" ],
      "timeoutInMinutes" : 600
    },
    "read" : {
      "permissions" : [ "rds:DescribeDBEngineVersions" ]
    },
    "update" : {
      "permissions" : [ "rds:AddTagsToResource", "rds:DescribeDBEngineVersions", "rds:ModifyCustomDBEngineVersion", "rds:RemoveTagsFromResource" ],
      "timeoutInMinutes" : 600
    },
    "delete" : {
      "permissions" : [ "rds:DeleteCustomDBEngineVersion", "rds:DescribeDBEngineVersions" ],
      "timeoutInMinutes" : 600
    },
    "list" : {
      "permissions" : [ "rds:DescribeDBEngineVersions" ]
    }
  }
}