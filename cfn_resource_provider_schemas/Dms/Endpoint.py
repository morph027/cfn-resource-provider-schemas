SCHEMA = {
  "typeName" : "AWS::DMS::Endpoint",
  "description" : "Resource Type definition for AWS::DMS::Endpoint",
  "additionalProperties" : False,
  "properties" : {
    "SybaseSettings" : {
      "$ref" : "#/definitions/SybaseSettings"
    },
    "RedisSettings" : {
      "$ref" : "#/definitions/RedisSettings"
    },
    "OracleSettings" : {
      "$ref" : "#/definitions/OracleSettings"
    },
    "KafkaSettings" : {
      "$ref" : "#/definitions/KafkaSettings"
    },
    "Port" : {
      "type" : "integer"
    },
    "MySqlSettings" : {
      "$ref" : "#/definitions/MySqlSettings"
    },
    "S3Settings" : {
      "$ref" : "#/definitions/S3Settings"
    },
    "ResourceIdentifier" : {
      "type" : "string"
    },
    "KinesisSettings" : {
      "$ref" : "#/definitions/KinesisSettings"
    },
    "SslMode" : {
      "type" : "string"
    },
    "RedshiftSettings" : {
      "$ref" : "#/definitions/RedshiftSettings"
    },
    "EndpointType" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Password" : {
      "type" : "string"
    },
    "MongoDbSettings" : {
      "$ref" : "#/definitions/MongoDbSettings"
    },
    "IbmDb2Settings" : {
      "$ref" : "#/definitions/IbmDb2Settings"
    },
    "KmsKeyId" : {
      "type" : "string"
    },
    "ExternalId" : {
      "type" : "string"
    },
    "DatabaseName" : {
      "type" : "string"
    },
    "NeptuneSettings" : {
      "$ref" : "#/definitions/NeptuneSettings"
    },
    "ElasticsearchSettings" : {
      "$ref" : "#/definitions/ElasticsearchSettings"
    },
    "EngineName" : {
      "type" : "string"
    },
    "DocDbSettings" : {
      "$ref" : "#/definitions/DocDbSettings"
    },
    "DynamoDbSettings" : {
      "$ref" : "#/definitions/DynamoDbSettings"
    },
    "Username" : {
      "type" : "string"
    },
    "MicrosoftSqlServerSettings" : {
      "$ref" : "#/definitions/MicrosoftSqlServerSettings"
    },
    "GcpMySQLSettings" : {
      "$ref" : "#/definitions/GcpMySQLSettings"
    },
    "ServerName" : {
      "type" : "string"
    },
    "ExtraConnectionAttributes" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "EndpointIdentifier" : {
      "type" : "string"
    },
    "CertificateArn" : {
      "type" : "string"
    },
    "PostgreSqlSettings" : {
      "$ref" : "#/definitions/PostgreSqlSettings"
    }
  },
  "definitions" : {
    "RedisSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SslSecurityProtocol" : {
          "type" : "string"
        },
        "AuthUserName" : {
          "type" : "string"
        },
        "ServerName" : {
          "type" : "string"
        },
        "Port" : {
          "type" : "number"
        },
        "SslCaCertificateArn" : {
          "type" : "string"
        },
        "AuthPassword" : {
          "type" : "string"
        },
        "AuthType" : {
          "type" : "string"
        }
      }
    },
    "SybaseSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        }
      }
    },
    "IbmDb2Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LoadTimeout" : {
          "type" : "integer"
        },
        "SetDataCaptureChanges" : {
          "type" : "boolean"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "KeepCsvFiles" : {
          "type" : "boolean"
        },
        "CurrentLsn" : {
          "type" : "string"
        },
        "MaxKBytesPerRead" : {
          "type" : "integer"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "WriteBufferSize" : {
          "type" : "integer"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        }
      }
    },
    "OracleSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AsmPassword" : {
          "type" : "string"
        },
        "DirectPathParallelLoad" : {
          "type" : "boolean"
        },
        "AdditionalArchivedLogDestId" : {
          "type" : "integer"
        },
        "SpatialDataOptionToGeoJsonFunctionName" : {
          "type" : "string"
        },
        "ReplacePathPrefix" : {
          "type" : "boolean"
        },
        "FailTasksOnLobTruncation" : {
          "type" : "boolean"
        },
        "AsmServer" : {
          "type" : "string"
        },
        "SecretsManagerOracleAsmAccessRoleArn" : {
          "type" : "string"
        },
        "OraclePathPrefix" : {
          "type" : "string"
        },
        "ReadAheadBlocks" : {
          "type" : "integer"
        },
        "StandbyDelayTime" : {
          "type" : "integer"
        },
        "AllowSelectNestedTables" : {
          "type" : "boolean"
        },
        "AddSupplementalLogging" : {
          "type" : "boolean"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "UseBFile" : {
          "type" : "boolean"
        },
        "EnableHomogenousTablespace" : {
          "type" : "boolean"
        },
        "AsmUser" : {
          "type" : "string"
        },
        "UseDirectPathFullLoad" : {
          "type" : "boolean"
        },
        "SecurityDbEncryption" : {
          "type" : "string"
        },
        "ParallelAsmReadThreads" : {
          "type" : "integer"
        },
        "ArchivedLogDestId" : {
          "type" : "integer"
        },
        "UsePathPrefix" : {
          "type" : "string"
        },
        "UseLogminerReader" : {
          "type" : "boolean"
        },
        "SecurityDbEncryptionName" : {
          "type" : "string"
        },
        "DirectPathNoLog" : {
          "type" : "boolean"
        },
        "SecretsManagerOracleAsmSecretId" : {
          "type" : "string"
        },
        "CharLengthSemantics" : {
          "type" : "string"
        },
        "NumberDatatypeScale" : {
          "type" : "integer"
        },
        "ReadTableSpaceName" : {
          "type" : "boolean"
        },
        "AccessAlternateDirectly" : {
          "type" : "boolean"
        },
        "UseAlternateFolderForOnline" : {
          "type" : "boolean"
        },
        "ArchivedLogsOnly" : {
          "type" : "boolean"
        },
        "ExtraArchivedLogDestIds" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "integer"
          }
        },
        "RetryInterval" : {
          "type" : "integer"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        }
      }
    },
    "KafkaSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Broker" : {
          "type" : "string"
        },
        "SaslPassword" : {
          "type" : "string"
        },
        "MessageFormat" : {
          "type" : "string"
        },
        "SslClientCertificateArn" : {
          "type" : "string"
        },
        "IncludeTransactionDetails" : {
          "type" : "boolean"
        },
        "SecurityProtocol" : {
          "type" : "string"
        },
        "IncludeTableAlterOperations" : {
          "type" : "boolean"
        },
        "SslCaCertificateArn" : {
          "type" : "string"
        },
        "IncludeControlDetails" : {
          "type" : "boolean"
        },
        "IncludePartitionValue" : {
          "type" : "boolean"
        },
        "NoHexPrefix" : {
          "type" : "boolean"
        },
        "SslClientKeyArn" : {
          "type" : "string"
        },
        "SslClientKeyPassword" : {
          "type" : "string"
        },
        "SaslUserName" : {
          "type" : "string"
        },
        "MessageMaxBytes" : {
          "type" : "integer"
        },
        "Topic" : {
          "type" : "string"
        },
        "PartitionIncludeSchemaTable" : {
          "type" : "boolean"
        },
        "IncludeNullAndEmpty" : {
          "type" : "boolean"
        }
      }
    },
    "MySqlSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServerTimezone" : {
          "type" : "string"
        },
        "EventsPollInterval" : {
          "type" : "integer"
        },
        "ParallelLoadThreads" : {
          "type" : "integer"
        },
        "AfterConnectScript" : {
          "type" : "string"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "TargetDbType" : {
          "type" : "string"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "CleanSourceMetadataOnMismatch" : {
          "type" : "boolean"
        }
      }
    },
    "NeptuneSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxRetryCount" : {
          "type" : "integer"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "S3BucketFolder" : {
          "type" : "string"
        },
        "ErrorRetryDuration" : {
          "type" : "integer"
        },
        "IamAuthEnabled" : {
          "type" : "boolean"
        },
        "S3BucketName" : {
          "type" : "string"
        },
        "ServiceAccessRoleArn" : {
          "type" : "string"
        }
      }
    },
    "ElasticsearchSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EndpointUri" : {
          "type" : "string"
        },
        "ErrorRetryDuration" : {
          "type" : "integer"
        },
        "FullLoadErrorPercentage" : {
          "type" : "integer"
        },
        "ServiceAccessRoleArn" : {
          "type" : "string"
        }
      }
    },
    "S3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimestampColumnName" : {
          "type" : "string"
        },
        "EnableStatistics" : {
          "type" : "boolean"
        },
        "DatePartitionSequence" : {
          "type" : "string"
        },
        "CsvNullValue" : {
          "type" : "string"
        },
        "IncludeOpForFullLoad" : {
          "type" : "boolean"
        },
        "CdcInsertsAndUpdates" : {
          "type" : "boolean"
        },
        "BucketName" : {
          "type" : "string"
        },
        "ServerSideEncryptionKmsKeyId" : {
          "type" : "string"
        },
        "UseTaskStartTimeForFullLoadTimestamp" : {
          "type" : "boolean"
        },
        "GlueCatalogGeneration" : {
          "type" : "boolean"
        },
        "DataFormat" : {
          "type" : "string"
        },
        "CsvDelimiter" : {
          "type" : "string"
        },
        "AddTrailingPaddingCharacter" : {
          "type" : "boolean"
        },
        "IgnoreHeaderRows" : {
          "type" : "integer"
        },
        "CannedAclForObjects" : {
          "type" : "string"
        },
        "Rfc4180" : {
          "type" : "boolean"
        },
        "ServiceAccessRoleArn" : {
          "type" : "string"
        },
        "ParquetTimestampInMillisecond" : {
          "type" : "boolean"
        },
        "PreserveTransactions" : {
          "type" : "boolean"
        },
        "BucketFolder" : {
          "type" : "string"
        },
        "DatePartitionDelimiter" : {
          "type" : "string"
        },
        "EncodingType" : {
          "type" : "string"
        },
        "AddColumnName" : {
          "type" : "boolean"
        },
        "CdcMinFileSize" : {
          "type" : "integer"
        },
        "ParquetVersion" : {
          "type" : "string"
        },
        "ExternalTableDefinition" : {
          "type" : "string"
        },
        "UseCsvNoSupValue" : {
          "type" : "boolean"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "CdcPath" : {
          "type" : "string"
        },
        "CsvNoSupValue" : {
          "type" : "string"
        },
        "CdcMaxBatchInterval" : {
          "type" : "integer"
        },
        "CsvRowDelimiter" : {
          "type" : "string"
        },
        "RowGroupLength" : {
          "type" : "integer"
        },
        "DataPageSize" : {
          "type" : "integer"
        },
        "DatePartitionEnabled" : {
          "type" : "boolean"
        },
        "DictPageSizeLimit" : {
          "type" : "integer"
        },
        "CompressionType" : {
          "type" : "string"
        },
        "DatePartitionTimezone" : {
          "type" : "string"
        },
        "CdcInsertsOnly" : {
          "type" : "boolean"
        },
        "ExpectedBucketOwner" : {
          "type" : "string"
        },
        "EncryptionMode" : {
          "type" : "string"
        }
      }
    },
    "DocDbSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "DocsToInvestigate" : {
          "type" : "integer"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "ExtractDocId" : {
          "type" : "boolean"
        },
        "NestingLevel" : {
          "type" : "string"
        }
      }
    },
    "DynamoDbSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceAccessRoleArn" : {
          "type" : "string"
        }
      }
    },
    "KinesisSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MessageFormat" : {
          "type" : "string"
        },
        "IncludeTransactionDetails" : {
          "type" : "boolean"
        },
        "IncludeTableAlterOperations" : {
          "type" : "boolean"
        },
        "IncludeControlDetails" : {
          "type" : "boolean"
        },
        "IncludePartitionValue" : {
          "type" : "boolean"
        },
        "StreamArn" : {
          "type" : "string"
        },
        "ServiceAccessRoleArn" : {
          "type" : "string"
        },
        "NoHexPrefix" : {
          "type" : "boolean"
        },
        "PartitionIncludeSchemaTable" : {
          "type" : "boolean"
        },
        "IncludeNullAndEmpty" : {
          "type" : "boolean"
        }
      }
    },
    "GcpMySQLSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AfterConnectScript" : {
          "type" : "string"
        },
        "Port" : {
          "type" : "integer"
        },
        "DatabaseName" : {
          "type" : "string"
        },
        "CleanSourceMetadataOnMismatch" : {
          "type" : "boolean"
        },
        "ServerTimezone" : {
          "type" : "string"
        },
        "EventsPollInterval" : {
          "type" : "integer"
        },
        "ParallelLoadThreads" : {
          "type" : "integer"
        },
        "Username" : {
          "type" : "string"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "ServerName" : {
          "type" : "string"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "Password" : {
          "type" : "string"
        }
      }
    },
    "MicrosoftSqlServerSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ReadBackupOnly" : {
          "type" : "boolean"
        },
        "TlogAccessMode" : {
          "type" : "string"
        },
        "BcpPacketSize" : {
          "type" : "integer"
        },
        "Port" : {
          "type" : "integer"
        },
        "SafeguardPolicy" : {
          "type" : "string"
        },
        "UseThirdPartyBackupDevice" : {
          "type" : "boolean"
        },
        "DatabaseName" : {
          "type" : "string"
        },
        "UseBcpFullLoad" : {
          "type" : "boolean"
        },
        "Username" : {
          "type" : "string"
        },
        "QuerySingleAlwaysOnNode" : {
          "type" : "boolean"
        },
        "ServerName" : {
          "type" : "string"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "ControlTablesFileGroup" : {
          "type" : "string"
        },
        "ForceLobLookup" : {
          "type" : "boolean"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "TrimSpaceInChar" : {
          "type" : "boolean"
        },
        "Password" : {
          "type" : "string"
        }
      }
    },
    "RedshiftSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionTimeout" : {
          "type" : "integer"
        },
        "MapBooleanAsBoolean" : {
          "type" : "boolean"
        },
        "AfterConnectScript" : {
          "type" : "string"
        },
        "FileTransferUploadStreams" : {
          "type" : "integer"
        },
        "BucketName" : {
          "type" : "string"
        },
        "ServerSideEncryptionKmsKeyId" : {
          "type" : "string"
        },
        "ExplicitIds" : {
          "type" : "boolean"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "TruncateColumns" : {
          "type" : "boolean"
        },
        "ServiceAccessRoleArn" : {
          "type" : "string"
        },
        "ReplaceChars" : {
          "type" : "string"
        },
        "TimeFormat" : {
          "type" : "string"
        },
        "BucketFolder" : {
          "type" : "string"
        },
        "ReplaceInvalidChars" : {
          "type" : "string"
        },
        "RemoveQuotes" : {
          "type" : "boolean"
        },
        "LoadTimeout" : {
          "type" : "integer"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "TrimBlanks" : {
          "type" : "boolean"
        },
        "DateFormat" : {
          "type" : "string"
        },
        "CompUpdate" : {
          "type" : "boolean"
        },
        "AcceptAnyDate" : {
          "type" : "boolean"
        },
        "WriteBufferSize" : {
          "type" : "integer"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "CaseSensitiveNames" : {
          "type" : "boolean"
        },
        "EmptyAsNull" : {
          "type" : "boolean"
        },
        "EncryptionMode" : {
          "type" : "string"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "MongoDbSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Port" : {
          "type" : "integer"
        },
        "ExtractDocId" : {
          "type" : "string"
        },
        "DatabaseName" : {
          "type" : "string"
        },
        "AuthSource" : {
          "type" : "string"
        },
        "AuthMechanism" : {
          "type" : "string"
        },
        "Username" : {
          "type" : "string"
        },
        "DocsToInvestigate" : {
          "type" : "string"
        },
        "ServerName" : {
          "type" : "string"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "AuthType" : {
          "type" : "string"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "Password" : {
          "type" : "string"
        },
        "NestingLevel" : {
          "type" : "string"
        }
      }
    },
    "PostgreSqlSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PluginName" : {
          "type" : "string"
        },
        "MapBooleanAsBoolean" : {
          "type" : "boolean"
        },
        "AfterConnectScript" : {
          "type" : "string"
        },
        "ExecuteTimeout" : {
          "type" : "integer"
        },
        "DdlArtifactsSchema" : {
          "type" : "string"
        },
        "FailTasksOnLobTruncation" : {
          "type" : "boolean"
        },
        "HeartbeatEnable" : {
          "type" : "boolean"
        },
        "BabelfishDatabaseName" : {
          "type" : "string"
        },
        "DatabaseMode" : {
          "type" : "string"
        },
        "CaptureDdls" : {
          "type" : "boolean"
        },
        "MaxFileSize" : {
          "type" : "integer"
        },
        "HeartbeatFrequency" : {
          "type" : "integer"
        },
        "SecretsManagerSecretId" : {
          "type" : "string"
        },
        "SecretsManagerAccessRoleArn" : {
          "type" : "string"
        },
        "HeartbeatSchema" : {
          "type" : "string"
        },
        "SlotName" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "EndpointType", "EngineName" ],
  "createOnlyProperties" : [ "/properties/KmsKeyId", "/properties/ResourceIdentifier" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/ExternalId" ]
}